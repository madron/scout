import factory
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
