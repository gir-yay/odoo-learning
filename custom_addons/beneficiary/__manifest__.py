{
    'name': 'Beneficiary',
    'version': '1.0.0',
    'category': '',
    'author': 'gg',
    'depends': [
        'base', 'mail', 'hr'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/beneficiary_view.xml',
        'views/disability_view.xml',
        'views/section_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}
