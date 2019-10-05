import factory
from decimal import Decimal
from .. import models


class TypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Type

    id = factory.Sequence(lambda n: 'cloth{0}'.format(n))
    name = 'shirt'


class ConditionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Condition

    id = factory.Sequence(lambda n: 'cloth{0}'.format(n))
    order = factory.Sequence(lambda n: n)
    name = 'shirt'


class CatalogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Catalog

    type = factory.SubFactory(TypeFactory)
    condition = factory.SubFactory(ConditionFactory)
    price = Decimal('0.00')


class InventoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Inventory

    catalog = factory.SubFactory(CatalogFactory)
    quantity = 1
