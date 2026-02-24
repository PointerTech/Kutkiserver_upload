# -*- coding: utf-8 -*-
{
    'name': "crystal_custom_bill",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
    Custom billing format for crystal cleaner
    """,

    'author': "Kutki Tech.",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '18.0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'reports/report_templates.xml',
        'reports/report_invoice.xml',
        'views/account_move_add_field_view.xml',
    ],

}

