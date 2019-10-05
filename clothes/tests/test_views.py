from django.urls import reverse
from django.test import TestCase
from . import factories


class InventoryTest(TestCase):
    def setUp(self):
        self.url = reverse('clothes:inventory')

    def test_empty(self):
        factories.InventoryFactory(
            catalog__type__name='Shirt',
            quantity=1
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Shirt')
