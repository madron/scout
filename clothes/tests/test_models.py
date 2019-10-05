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


class InventoryModelTest(TestCase):
    def test_str(self):
        obj = factories.InventoryFactory(type__name='shirt', condition__name='good', quantity=3)
        self.assertEqual(str(obj), 'shirt - good')