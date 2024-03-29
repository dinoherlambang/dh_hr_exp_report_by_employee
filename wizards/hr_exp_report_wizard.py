from odoo import models, fields, api, _
from odoo.exceptions import UserError


class HRExpenseReport(models.TransientModel):
    _name = 'hr.expense.report.wizard'

    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date", required=True)
    employee_ids = fields.Many2many('hr.employee', string="Employee", required=True)

    # def print_hr_exp_report(self):
    #     hr_expenses = self.env['hr.expense'].search([])
    #     hr_expense_groupby_dict = {}
    #     for employee in self.employee_ids:
    #         filtered_hr_expenses = list(filter(lambda x: x.employee_id == employee, hr_expenses))
    #         filtered_by_date = list(filter(lambda x: x.date >= self.start_date and x.date <= self.end_date, filtered_hr_expenses))
    #         hr_expense_groupby_dict[employee.name] = filtered_by_date

    #     final_dist = {}
    #     for employee in hr_expense_groupby_dict.keys():
    #         expense_data = []
    #         for expense in hr_expense_groupby_dict[employee]:
    #             temp_data = []
    #             temp_data.append(expense.name)
    #             temp_data.append(expense.date)
    #             temp_data.append(expense.description)
    #             temp_data.append(expense.total_amount)
    #             expense_data.append(temp_data)
    #         final_dist[employee] = expense_data
    #     datas = {
    #         'ids': self,
    #         'model': 'hr.expense.report.wizard',
    #         'form': final_dist,
    #         'start_date': self.start_date,
    #         'end_date': self.end_date
    #     }
    #     return self.env.ref('dh_hr_exp_report_by_employee.action_report_by_employee').report_action([], data=datas)



################


    def print_hr_exp_report(self):
        hr_expenses = self.env['hr.expense'].search([])
        hr_expense_groupby_dict = {}
        for employee in self.employee_ids:
            filtered_hr_expenses = list(filter(lambda x: x.employee_id == employee, hr_expenses))
            filtered_by_date = list(filter(lambda x: x.date >= self.start_date and x.date <= self.end_date, filtered_hr_expenses))
            if filtered_by_date:  # Check if the list is not empty
                hr_expense_groupby_dict[employee.name] = filtered_by_date

        if not hr_expense_groupby_dict:
            raise UserError(_("No records found in the selected date range."))

        final_dist = {}
        for employee in hr_expense_groupby_dict.keys():
            expense_data = []
            for expense in hr_expense_groupby_dict[employee]:
                temp_data = []
                temp_data.append(expense.name)
                temp_data.append(expense.date)
                temp_data.append(expense.description)
                temp_data.append(expense.total_amount)
                expense_data.append(temp_data)
            final_dist[employee] = expense_data

        datas = {
            'ids': self,
            'model': 'hr.expense.report.wizard',
            'form': final_dist,
            'start_date': self.start_date,
            'end_date': self.end_date
        }
        return self.env.ref('dh_hr_exp_report_by_employee.action_report_by_employee').report_action([], data=datas)

