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


@admin.register(models.Inventory)
class InventoryAdmin(VersionAdmin):
    list_display = ('type', 'condition', 'quantity')
    list_display_links = ('type', 'condition')
    list_editable = ('quantity',)
    search_fields = ('type__name', 'condition__name')
