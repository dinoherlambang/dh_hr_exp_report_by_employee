# -*- coding: utf-8 -*-
# from odoo import http


# class DhHrExpenseReport(http.Controller):
#     @http.route('/dh_hr_expense_report/dh_hr_expense_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dh_hr_expense_report/dh_hr_expense_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dh_hr_expense_report.listing', {
#             'root': '/dh_hr_expense_report/dh_hr_expense_report',
#             'objects': http.request.env['dh_hr_expense_report.dh_hr_expense_report'].search([]),
#         })

#     @http.route('/dh_hr_expense_report/dh_hr_expense_report/objects/<model("dh_hr_expense_report.dh_hr_expense_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dh_hr_expense_report.object', {
#             'object': obj
#         })
