from django.views.generic import TemplateView
from . import models


class InventoryView(TemplateView):
    template_name = 'clothes/inventory.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        qs = models.Inventory.objects.filter(quantity__gt=0)
        qs = qs.order_by('catalog__type__name')
        data['inventory'] = qs
        return data
