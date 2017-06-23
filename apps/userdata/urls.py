# coding: utf-8
import json
from django.conf.urls import url, include

from rest_framework import routers

from userdata.views import PresenceViewSet, StepsViewSet, SleepViewSet


router = routers.DefaultRouter()
router.register(r'presence', PresenceViewSet)
router.register(r'steps', StepsViewSet)
router.register(r'sleep', SleepViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
