class ProductPerWarehouse(models.Model):
    _name = 'custom.inventory.by.warehouse'
    _description = 'Productos por Bodega'

    product_id = fields.Many2one('product.product', string='Producto')
    location_id = fields.Many2one('stock.location', string='Ubicación (Bodega)')
    quantity = fields.Float(string='Cantidad Disponible')

    @api.model
    def actualizar_existencias(self):
        # stock.quant tiene la cantidad real de productos por ubicación
        quants = self.env['stock.quant'].search([])

        for quant in quants:
            self.create({
                'product_id': quant.product_id.id,
                'location_id': quant.location_id.id,
                'quantity': quant.quantity,
            })
