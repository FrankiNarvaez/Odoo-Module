from odoo import models, fields

class SaleOrderType(models.Model):
    _name = 'sale.order.type'
    _description = 'Sale Order Type'

    name = fields.Char(required=True)
    code = fields.Char(required=True)
