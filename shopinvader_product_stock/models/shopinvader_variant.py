# Copyright 2018 Akretion (http://www.akretion.com)
# Copyright 2018 ACSONE SA/NV
# Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from collections import defaultdict

from odoo import api, fields, models


class ShopinvaderVariant(models.Model):
    _inherit = "shopinvader.variant"

    stock_data = fields.Serialized(compute="_compute_stock_data")

    def _get_stock_export_key(self):
        self.ensure_one()
        line = self.env["ir.exports.line"].search(
            [
                ("export_id", "=", self.index_id.exporter_id.id),
                ("name", "=", "stock_data"),
            ]
        )
        if line.alias:
            return line.alias.split(":")[1]
        else:
            return line.name

    def _prepare_stock_data(self):
        self.ensure_one()
        stock_field = self.backend_id.product_stock_field_id.name
        return {"qty": self[stock_field]}
        # stock_field = self.backend_id.product_stock_field_id
        # if stock_field.model == "product.template":
        #     qty = self[stock_field.name]
        # else:  # "product.product"
        #     qty = self.record_id[stock_field.name]
        # return {"qty": qty}

    @api.multi
    def _compute_stock_data(self):
        result = defaultdict(dict)
        for backend in self.mapped("backend_id"):
            loc_records = self.filtered(lambda s: s.backend_id == backend)
            for (
                wh_key,
                wh_ids,
            ) in backend._get_warehouse_list_for_export().items():

                for loc_record in loc_records.with_context(warehouse=wh_ids):
                    result[loc_record.id][
                        wh_key
                    ] = loc_record._prepare_stock_data()
        for record in self:
            record.stock_data = result[record.id]
