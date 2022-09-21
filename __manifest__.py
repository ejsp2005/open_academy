# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """
        Description of Open Academy's module
    """,

    'description': """
        Description of Open Academy's module
    """,

    'author': "Ernesto J. Suárez Pons",
    'website': "http://www.ejsp.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'license': 'LGPL-3',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/res_partner.xml',
        'views/sessions_views.xml',
        'views/groups_views.xml',
        'views/courses_views.xml',
        'views/menu_views.xml',
        'security/ir.model.access.csv',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    
    'auto_install': False,
    'application': True,
}
