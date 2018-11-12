# -*- coding: utf-8 -*-
# Copyright 2017 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ShopinvaderVariant(models.Model):
    _inherit = 'shopinvader.variant'

    hierarchical_categories = fields.Serialized(
        compute='_compute_shopinvader_category',
        string='Hierarchical Categories')

    def _compute_shopinvader_category(self):
        super(ShopinvaderVariant, self)._compute_shopinvader_category()

        def get_full_name(categ):
            result = []
            while categ:
                result.insert(0, categ.name)
                categ = categ.parent_id
            return ' > '.join(result)

        for record in self:
            record.hierarchical_categories = {}
            for categ in record.shopinvader_categ_ids:
                record.hierarchical_categories['lvl%s' % categ.level] =\
                    get_full_name(categ.record_id)

    @api.multi
    def _unbind(self):
        """
        Action to unbind current recordset
        :return: bool
        """
        result = super(ShopinvaderVariant, self)._unbind()
        for record in self:
            record.with_delay().unsynchronize()
        return result

    @api.multi
    def _bind(self):
        """
        Action to bind current recordset
        :return:
        """
        result = super(ShopinvaderVariant, self)._bind()
        for record in self:
            record.with_delay().export()
        return result
