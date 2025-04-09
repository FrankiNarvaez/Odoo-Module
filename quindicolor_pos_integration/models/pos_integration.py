from odoo import models, fields, api

class StockWarehouse(models.Model):
    _inherit = 'stock.warehouse'

    # Añadir campo para priorizar tiendas físicas
    pos_priority = fields.Integer(string="Prioridad en PoS", default=1)
