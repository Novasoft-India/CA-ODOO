# -*- coding: utf-8 -*-
{
    'name': "CA",

    'summary': """
        Module for Charted Accountants""",

    'description': """
        For managing their day-to-day activities.
        GitHub Repo : https://github.com/Novasoft-India/CA-ODOO.git
    """,

    'author': "Novasoft Consultancy Services Pvt. Ltd.",
    'website': "http://www.novasoftindia.com",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','project','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml','ca_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}