# Copyright 2021 Camptocamp (http://www.camptocamp.com).
# @author Simone Orsi <simahawk@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.addons.component.core import Component


class PartnerAccess(Component):
    _inherit = "shopinvader.partner.access"

    def permissions(self):
        perm = super().permissions()
        perm["wishlist"] = self._wishlist_perm()
        return perm

    def _wishlist_perm(self):
        return {"create": True, "read": True, "update": True, "delete": True}

    def for_wishlist(self, wishlist):
        return {"read": True, "update": True, "delete": True}
