# -*- coding: utf-8 -*-
# Copyright 2020 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResPartnerExtra(models.Model):
    _name = "res.partner.extra"

    partner_id = fields.Many2one("res.partner", "Partner")
    extra = fields.Char()
