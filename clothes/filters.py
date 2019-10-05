from django.contrib import admin
from django.utils.translation import ugettext as _
from . import models


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
