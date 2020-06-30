# -*- coding: utf-8 -*-
# Copyright 2020 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import SavepointCase

from odoo_test_helper import FakeModelLoader


class TestMixin(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super(TestMixin, cls).setUpClass()
        cls.loader = FakeModelLoader(cls.env, cls.__module__)
        cls.loader.backup_registry()
        from .models.res_partner import ResPartner

        cls.loader.update_registry((ResPartner,))

    @classmethod
    def tearDownClass(cls):
        cls.loader.restore_registry()
        super(TestMixin, cls).tearDownClass()

    def test_create(self):
        partner = self.env["res.partner"].create({"name": "BAR", "test_char": "youhou"})
        self.assertEqual(partner.name, "FOO-BAR")
        self.assertEqual(partner.test_char, "youhou")
