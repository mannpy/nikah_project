# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils.translation import activate


class TestHomePage(TestCase):

    def test_uses_index_template(self):
        activate('ru')
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "nikah/index.html")

    def test_uses_base_template(self):
        activate('ru')
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "base.html")
