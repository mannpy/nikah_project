from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils.translation import activate
from .models import Category, Item


class TestHomePage(TestCase):

    def test_index_view_with_no_items(self):
        """
        If no items exist, an appropriate message should be displayed.
        """
        activate('en')
        response = self.client.get(reverse('main:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response, "There are no products in this category.")
        self.assertQuerysetEqual(response.context['items'], [])

    def test_index_view_with_items(self):
        activate('en')
        clothes_cat = Category.objects.create(name='Одежда')
        Item.objects.create(
            category=clothes_cat,
            name='Платье',
            description='Простое платье',
            price=1000,
            photo=None)
        response = self.client.get(reverse('main:home'))
        self.assertQuerysetEqual(
            response.context['items'],
            ['<Item: Платье>'])

    def test_index_view_with_no_slider(self):
        """
        If no items exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('main:home'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['slider'], [])

    def test_uses_index_template(self):
        response = self.client.get(reverse("main:home"))
        self.assertTemplateUsed(response, "main/index.html")

    def test_uses_base_template(self):
        response = self.client.get(reverse("main:home"))
        self.assertTemplateUsed(response, "base.html")
