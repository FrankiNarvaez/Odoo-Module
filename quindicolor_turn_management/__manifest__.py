{
    'name': 'Gestión de Turnos para QuindíColor',
    'version': '1.0',
    'summary': 'Sistema de gestión de turnos para puntos físicos de venta.',
    'description': 'Permite registrar, asignar y gestionar turnos de clientes en los puntos de venta físicos de QuindíColor.',
    'author': 'Joshua',
    'license': 'LGPL-3',
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/customer_turn_views.xml',
    ],
    'installable': True,
    'application': True,
}
