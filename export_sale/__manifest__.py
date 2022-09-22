{
    'name': 'Export Sales',
    'version': '1.0',
    'category': 'Extra Tools',
    'summary': 'This module shows exported sales',
    'description': """
   
    """,
    'sequence':-500,
    'depends': ['sale_management'],
    'data': [
    'security/ir.model.access.csv',
    #'views/sale_export_view.xml',
    'wizard/date_views_wizard.xml',
    'wizard/o2m_wizard_views.xml',
    'views/res_config_views.xml',
    'views/m2m_views.xml',
    

    ],
    'installable':True,
    'auto_install':False,
    'application':True,
    'license': 'LGPL-3',
}