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
        obj = factories.TypeFactory()
        url = reverse('admin:clothes_type_change', args=(obj.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        obj = factories.TypeFactory()
        url = reverse('admin:clothes_type_delete', args=(obj.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class ConditionAdminTest(TestCase):
    def setUp(self):
        UserFactory()
        self.assertTrue(self.client.login(username='test', password='pass'))
        self.list = reverse('admin:clothes_condition_changelist')

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
        obj = factories.ConditionFactory()
        url = reverse('admin:clothes_condition_change', args=(obj.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        obj = factories.ConditionFactory()
        url = reverse('admin:clothes_condition_delete', args=(obj.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class CatalogAdminTest(TestCase):
    def setUp(self):
        UserFactory()
        self.assertTrue(self.client.login(username='test', password='pass'))
        self.list = reverse('admin:clothes_catalog_changelist')

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
        obj = factories.CatalogFactory()
        url = reverse('admin:clothes_catalog_change', args=(obj.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        obj = factories.CatalogFactory()
        url = reverse('admin:clothes_catalog_delete', args=(obj.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class InventoryAdminTest(TestCase):
    def setUp(self):
        UserFactory()
        self.assertTrue(self.client.login(username='test', password='pass'))
        self.list = reverse('admin:clothes_inventory_changelist')

    def test_list(self):
        response = self.client.get(self.list)
        self.assertEqual(response.status_code, 200)

    def test_search(self):
        data = dict(q='text')
        response = self.client.get(self.list, data)
        self.assertEqual(response.status_code, 200)

    def test_add(self):
        url = reverse('admin:clothes_inventory_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail(self):
        obj = factories.InventoryFactory()
        url = reverse('admin:clothes_inventory_change', args=(obj.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        obj = factories.InventoryFactory()
        url = reverse('admin:clothes_inventory_delete', args=(obj.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
