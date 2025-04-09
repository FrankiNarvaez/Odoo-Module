from odoo import models, fields

class PosConfig(models.Model):
    _inherit = 'pos.config'

    available_stock_threshold = fields.Integer(
        string="Available Stock Threshold",
        help="Threshold for available stock in POS."
    )
