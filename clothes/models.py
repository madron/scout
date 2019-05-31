from django.db import models
from django.utils.translation import ugettext_lazy as _


class Type(models.Model):
    id = models.CharField(_('id'), max_length=50, primary_key=True, db_index=True)
    name = models.CharField(_('name'), max_length=50, db_index=True)

    class Meta:
        verbose_name = _('type')
        verbose_name_plural = _('types')
        ordering = ['id']

    def __str__(self):
        return str(self.name)


class Condition(models.Model):
    order = models.IntegerField(_('order'), db_index=True)
    id = models.CharField(_('id'), max_length=50, primary_key=True, db_index=True)
    name = models.CharField(_('name'), max_length=50, db_index=True)

    class Meta:
        verbose_name = _('condition')
        verbose_name_plural = _('conditions')
        ordering = ['order', 'id']

    def __str__(self):
        return str(self.name)


class Inventory(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name=_('type'))
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE, verbose_name=_('condition'))
    quantity = models.PositiveIntegerField(_('quantity'), default=0)

    class Meta:
        verbose_name = _('inventory')
        verbose_name_plural = _('inventory')
        ordering = ['type', 'condition']

    def __str__(self):
        return '{} - {}'.format(self.type, self.condition)
