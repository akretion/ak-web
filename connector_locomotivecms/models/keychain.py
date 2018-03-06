# -*- coding: utf-8 -*-
# Copyright 2017 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class KeychainAccount(models.Model):
    _inherit = 'keychain.account'

    namespace = fields.Selection(
        selection_add=[('locomotivecms', 'LocomotiveCMS')])

    def _locomotivecms_validate_data(self, data):
        return True
