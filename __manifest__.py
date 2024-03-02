# -*- coding: utf-8 -*-
{
    'name': 'HR Expense Report',
    'version': '13.0.0.0.1',
    'summary': 'Generate your HR expense reports by employee',
    'author': 'Dino Herlambang',
    'maintainer': 'Dino Herlambang',
    'Company': 'cybrein',
    'website': 'https://instagram.com/_dinoherlambang_',
    'depends': ['base', 'hr_expense'],
    'license': 'LGPL-3',
    'category': 'Human Resources',
    'data':[
        'wizards/hr_exp_report_wizard.xml',
        'reports/hr_exp_reports.xml',
        'reports/hr_exp_report_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
