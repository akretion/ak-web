# -*- coding: utf-8 -*-
# Copyright 2017 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


{
    "name": "Shopinvader Demo App",
    "version": "10.0.1.0.0",
    "author": "Akretion",
    "website": "www.akretion.com",
    "license": "AGPL-3",
    "category": "Generic Modules",
    "depends": [
        "shopinvader",
        "shopinvader_assortment",
        "shopinvader_guest_mode",
        "shopinvader_locomotive",
        "shopinvader_locomotive_guest_mode",
        "shopinvader_locomotive_elasticsearch",
        "shopinvader_delivery_carrier",
        "shopinvader_product_stock",
        "shopinvader_image",
        "shopinvader_elasticsearch",
        "shopinvader_payment_manual",
        "product_brand",
        #  This module is broken for now
        #  https://github.com/OCA/product-variant/issues/92
        #  'product_variant_default_code',
    ],
    "data": ["data/ir_export_product.xml"],
    "demo": ["demo/product_brand_demo.xml", "demo/product_product_demo.xml"],
    "installable": True,
    "application": True,
}
