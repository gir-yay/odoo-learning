{
    'name': 'Todo Task',
    'version': '1.0.0',
    'category': '',
    'author': 'gg',
    'depends': [
        'base', 'contacts'
    ],
    'data': [
        'views/base_menu.xml',
        'views/todo_task_view.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}