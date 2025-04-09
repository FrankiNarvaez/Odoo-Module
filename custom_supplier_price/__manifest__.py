{
    'name': 'Actualización de precios de proveedores',
    'version': '1.0',
    'summary': 'Actualiza precios de compra desde proveedores y notifica los cambios',
    'description': """
Este módulo extiende la funcionalidad estándar de Odoo para monitorear y actualizar automáticamente
los precios de compra de los proveedores, generando notificaciones en los productos afectados.
""",
    'category': 'Purchases',
    'author': 'Tu Nombre o Empresa',
    'website': 'https://tusitio.com',
    'depends': ['purchase', 'product', 'stock'],
    'data': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
