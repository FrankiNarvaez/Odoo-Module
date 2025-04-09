odoo.define('quindicolor_pos_integration.PosStockSync', function (require) {
    "use strict";

    const PosComponent = require('point_of_sale.PosComponent');
    const Registries = require('point_of_sale.Registries');

    class StockSyncButton extends PosComponent {
        async onClick() {
            await this.env.pos.syncStockFromServer(); // Sincronizar stock
            this.showNotification('Stock actualizado', 3000);
        }
    }
    StockSyncButton.template = 'StockSyncButton';
    Registries.Component.add(StockSyncButton);

    return { StockSyncButton };
});

