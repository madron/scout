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
