# coding: utf-8
from django.contrib import admin
from userdata.models import Sleep, Steps, Presence


admin.site.register(Sleep)
admin.site.register(Steps)
admin.site.register(Presence)
