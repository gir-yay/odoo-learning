{
    'name': 'App one',
    'version': '1.0.0',
    'category': '',
    'author': 'gg',
    'depends': [
        'base', 'sale_management'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/property_view.xml',
        'views/owner_view.xml',
        'views/tag_view.xml',
        'views/sale_order_view.xml',
        'reports/property_report.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'app_one/static/src/css/property.css',
                               ]
    },
    'images': ['static/description/home.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}