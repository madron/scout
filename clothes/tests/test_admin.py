from django.urls import reverse
from django.test import TestCase
from authentication.tests.factories import UserFactory
from . import factories
from .. import models


class TypeAdminTest(TestCase):
    def setUp(self):
        UserFactory()
        self.assertTrue(self.client.login(username='test', password='pass'))
        self.list = reverse('admin:clothes_type_changelist')
        self.pk = factories.TypeFactory().pk

    def test_list(self):
        response = self.client.get(self.list)
        self.assertEqual(response.status_code, 200)

    def test_search(self):
        data = dict(q='text')
        response = self.client.get(self.list, data)
        self.assertEqual(response.status_code, 200)

    def test_add(self):
        url = reverse('admin:clothes_type_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail(self):
        url = reverse('admin:clothes_type_change', args=(self.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        url = reverse('admin:clothes_type_delete', args=(self.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class ConditionAdminTest(TestCase):
    def setUp(self):
        UserFactory()
        self.assertTrue(self.client.login(username='test', password='pass'))
        self.list = reverse('admin:clothes_condition_changelist')
        self.pk = factories.ConditionFactory().pk

    def test_list(self):
        response = self.client.get(self.list)
        self.assertEqual(response.status_code, 200)

    def test_search(self):
        data = dict(q='text')
        response = self.client.get(self.list, data)
        self.assertEqual(response.status_code, 200)

    def test_add(self):
        url = reverse('admin:clothes_condition_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail(self):
        url = reverse('admin:clothes_condition_change', args=(self.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        url = reverse('admin:clothes_condition_delete', args=(self.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class CatalogAdminTest(TestCase):
    def setUp(self):
        UserFactory()
        self.assertTrue(self.client.login(username='test', password='pass'))
        self.list = reverse('admin:clothes_catalog_changelist')
        self.pk = factories.CatalogFactory().pk

    def test_list(self):
        response = self.client.get(self.list)
        self.assertEqual(response.status_code, 200)

    def test_search(self):
        data = dict(q='text')
        response = self.client.get(self.list, data)
        self.assertEqual(response.status_code, 200)

    def test_add(self):
        url = reverse('admin:clothes_catalog_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail(self):
        url = reverse('admin:clothes_catalog_change', args=(self.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        url = reverse('admin:clothes_catalog_delete', args=(self.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class InventoryAdminTest(TestCase):
    def setUp(self):
        UserFactory()
        self.assertTrue(self.client.login(username='test', password='pass'))
        self.list = reverse('admin:clothes_inventory_changelist')
        self.pk = factories.InventoryFactory().pk

    def test_list(self):
        response = self.client.get(self.list)
        self.assertEqual(response.status_code, 200)

    def test_search(self):
        data = dict(q='text')
        response = self.client.get(self.list, data)
        self.assertEqual(response.status_code, 200)

    def test_filter_type(self):
        factories.InventoryFactory(catalog__type__id='socks', catalog__type__name='Socks')
        data = dict(type='socks')
        response = self.client.get(self.list, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Socks')

    def test_add(self):
        url = reverse('admin:clothes_inventory_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail(self):
        url = reverse('admin:clothes_inventory_change', args=(self.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        url = reverse('admin:clothes_inventory_delete', args=(self.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
