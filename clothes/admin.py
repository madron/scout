from django.conf.urls import url
from django.contrib import admin
from django.utils.translation import ugettext as _
from reversion.admin import VersionAdmin
from . import models


@admin.register(models.Type)
class TypeAdmin(VersionAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


@admin.register(models.Condition)
class ConditionAdmin(VersionAdmin):
    list_display = ('order', 'id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


@admin.register(models.Catalog)
class CatalogAdmin(VersionAdmin):
    list_display = ('type', 'condition', 'price')
    list_display_links = ('type', 'condition')
    search_fields = ('type__name', 'condition__name')


class InventoryTypeFilter(admin.SimpleListFilter):
    title = _('type')
    parameter_name = 'type'

    def lookups(self, request, model_admin):
        types = models.Type.objects.order_by('id')
        return [(t.id, t.name) for t in types]

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            return queryset.filter(catalog__type=value)
        return queryset


@admin.register(models.Inventory)
class InventoryAdmin(VersionAdmin):
    list_display = ('catalog_type', 'catalog_condition', 'size', 'quantity', 'catalog_price')
    list_display_links = ('size',)
    list_editable = ('quantity',)
    list_filter = (InventoryTypeFilter,)
    search_fields = ('catalog__type__name', 'catalog__condition__name')
