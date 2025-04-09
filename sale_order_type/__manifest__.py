{
    'name': 'Sale Order Type',
    'version': '1.0',
    'summary': 'Custom sale order types',
    'description': 'Allows defining different sale order types and assigning them to quotations/orders.',
    'category': 'Sales',
    'author': 'TuNombre / QuindíColor',
    'depends': ['sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_type_view.xml',
    ],
    'installable': True,
    'application': False,
}
