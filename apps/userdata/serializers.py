# coding: utf-8
import json
from django.contrib.gis.db.models.fields import PointField as ModelPointField

from rest_framework import serializers
from rest_framework.fields import ModelField

from userdata.models import Presence, Steps, Sleep


class CustomPointField(ModelField):

    def to_representation(self, obj):
        return list(obj.point.coords)


class PresenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presence
        fields = ('id', 'time_start', 'time_end', 'point',)

    point = CustomPointField(ModelPointField)


class StepsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Steps
        fields = ('id', 'time_start', 'time_end', 'count',)


class SleepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sleep
        fields = ('id', 'time_start', 'time_end',)
