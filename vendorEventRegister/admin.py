"""Admin configuration for the vendorEventRegister app."""

from django.contrib import admin

from vendorEventRegister.models import Events

# Register your models here.
admin.site.register(Events)
