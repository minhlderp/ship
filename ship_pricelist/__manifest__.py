{
    'name': 'Ship Pricelist',
    'version': '1.0',
    'summary': 'Ship pricelist configuration',
    'description': 'Ship pricelist configuration',
    'category': 'Sale',
    'author': 'MinhLD',
    'license': 'LGPL-3',
    'depends': [
        'sale',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/service_type_view.xml',
        'views/country_state_menu.xml',
        'views/ship_pricelist.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
