# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class dh_hr_expense_report(models.Model):
#     _name = 'dh_hr_expense_report.dh_hr_expense_report'
#     _description = 'dh_hr_expense_report.dh_hr_expense_report'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
