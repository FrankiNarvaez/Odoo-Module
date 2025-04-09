from odoo import models, fields, api

class SupplierInfo(models.Model):
    _inherit = 'product.supplierinfo'

    # Hacemos tracking del precio para que sea visible en el chatter si activamos tracking en el campo
    price = fields.Float(string="Precio", tracking=True)

    @api.model
    def create(self, vals):
        record = super().create(vals)
        record._check_price_change(new_price=vals.get('price'), is_new=True)
        return record

    def write(self, vals):
        # Guardamos los precios antiguos antes del cambio
        old_prices = {rec.id: rec.price for rec in self}
        result = super().write(vals)
        for rec in self:
            old_price = old_prices.get(rec.id)
            if 'price' in vals and old_price != rec.price:
                rec._check_price_change(new_price=rec.price, old_price=old_price)
        return result

    def _check_price_change(self, new_price, old_price=None, is_new=False):
        # Componemos el mensaje
        mensaje = f"🔔 Precio de compra actualizado para el producto '{self.product_tmpl_id.name}' del proveedor '{self.name.name}':"
        if is_new:
            mensaje += f"\n➡️ Nuevo precio registrado: {new_price}"
        else:
            mensaje += f"\n➡️ Precio anterior: {old_price}\n➡️ Precio nuevo: {new_price}"

        # Mandamos el mensaje al chatter del producto
        self.product_tmpl_id.message_post(body=mensaje)
