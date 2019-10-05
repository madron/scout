from django.test import TestCase
from . import factories


class TypeModelTest(TestCase):
    def test_str(self):
        obj = factories.TypeFactory(name='Shoe')
        self.assertEqual(str(obj), 'Shoe')


class ConditionModelTest(TestCase):
    def test_str(self):
        obj = factories.ConditionFactory(name='good')
        self.assertEqual(str(obj), 'good')


class CatalogModelTest(TestCase):
    def test_str(self):
        obj = factories.CatalogFactory(type__name='shirt', condition__name='good')
        self.assertEqual(str(obj), 'shirt - good')


class InventoryModelTest(TestCase):
    def test_str(self):
        obj = factories.InventoryFactory(
            catalog__type__name='shirt',
            catalog__condition__name='good',
            size='M',
            quantity=3,
        )
        self.assertEqual(str(obj), 'shirt - good - M')
