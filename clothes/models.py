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


class Catalog(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name=_('type'))
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE, verbose_name=_('condition'))
    price = models.DecimalField(_('price'), max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = _('catalog')
        verbose_name_plural = _('catalog')
        ordering = ['type', 'condition']
        unique_together = [['type', 'condition']]

    def __str__(self):
        return '{} - {}'.format(self.type, self.condition)


class Inventory(models.Model):
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, verbose_name=_('catalog'))
    size = models.CharField(_('size'), max_length=50, blank=True)
    quantity = models.PositiveIntegerField(_('quantity'), default=0)

    class Meta:
        verbose_name = _('inventory')
        verbose_name_plural = _('inventory')
        ordering = ['catalog__type', 'size', 'catalog__condition']
        unique_together = [['catalog', 'size']]

    def __str__(self):
        return '{} - {}'.format(self.catalog, self.size)

    def catalog_type(self):
        return self.catalog.type
    catalog_type.short_description = _('type')
    catalog_type.admin_order_field = 'catalog__type'

    def catalog_condition(self):
        return self.catalog.condition
    catalog_condition.short_description = _('condition')
    catalog_condition.admin_order_field = 'catalog__condition'

    def catalog_price(self):
        return self.catalog.price
    catalog_price.short_description = _('price')
    catalog_price.admin_order_field = 'catalog__price'
