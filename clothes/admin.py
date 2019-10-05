from django.conf.urls import url
from django.contrib import admin
from django.utils.translation import ugettext as _
from reversion.admin import VersionAdmin
from . import filters
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


@admin.register(models.Inventory)
class InventoryAdmin(VersionAdmin):
    list_display = ('catalog_type', 'catalog_condition', 'size', 'quantity', 'catalog_price')
    list_display_links = ('size',)
    list_editable = ('quantity',)
    list_filter = (filters.InventoryTypeFilter,)
    search_fields = ('catalog__type__name', 'catalog__condition__name')
