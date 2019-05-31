from django.views.generic import TemplateView


class InventoryView(TemplateView):
    template_name = 'clothes/inventory.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        return data
