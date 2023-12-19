from django.contrib import admin
from .models import Device
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple


class DeviceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Device, DeviceAdmin)


