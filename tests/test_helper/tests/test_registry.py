# -*- coding: utf-8 -*-
# Copyright 2020 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import SavepointCase

from odoo_test_helper import FakeModelLoader


class TestMixin(SavepointCase):
    def test_update_and_restore(self):
        loader = FakeModelLoader(self.env, self.__module__)
        loader.backup_registry()
        from .models import ResPartner, ResPartnerExtra

        self.assertNotIn("res.partner.extra", self.env.registry)
        self.assertNotIn("test_char", self.env["res.partner"]._fields)

        loader.update_registry([ResPartner, ResPartnerExtra])
        self.assertIn("res.partner.extra", self.env.registry)
        self.assertIn("test_char", self.env["res.partner"]._fields)

        loader.restore_registry()
        self.assertNotIn("res.partner.extra", self.env.registry)
        self.assertNotIn("test_char", self.env["res.partner"]._fields)
