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
