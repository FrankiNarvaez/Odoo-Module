{
    'name': 'Integración PoS - Inventario QuindiColor',
    'version': '1.0',
    'summary': 'Sincroniza el inventario con el Punto de Venta en tiempo real',
    'category': 'Inventory',
    'assets': {
        'point_of_sale.assets': [
            'quindicolor_pos_integration/static/src/js/pos_stock_sync.js',
        ],
    },
    'depends': ['stock', 'point_of_sale'],
    'data': [
        'views/pos_integration_views.xml',
    ],
    'installable': True,
    'application': True,
}

