# coding: utf-8
import django_filters
from django_filters import rest_framework as filters

from rest_framework import viewsets

from userdata.models import Presence, Steps, Sleep
from userdata.serializers import PresenceSerializer, StepsSerializer, SleepSerializer


class UserdataFilterMixin(filters.FilterSet):
    time_start = django_filters.IsoDateTimeFilter(name='time_start', lookup_expr='gte')
    time_end = django_filters.IsoDateTimeFilter(name='time_start', lookup_expr='lte')


class PresenceFilter(UserdataFilterMixin, filters.FilterSet):
    class Meta:
        model = Presence
        fields = ['time_start', 'time_end']


class StepsFilter(UserdataFilterMixin, filters.FilterSet):
    class Meta:
        model = Steps
        fields = ['time_start', 'time_end']


class SleepFilter(UserdataFilterMixin, filters.FilterSet):
    class Meta:
        model = Sleep
        fields = ['time_start', 'time_end']


class PresenceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Presence.objects.all()
    serializer_class = PresenceSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = PresenceFilter


class StepsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Steps.objects.all()
    serializer_class = StepsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = StepsFilter


class SleepViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sleep.objects.all()
    serializer_class = SleepSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = SleepFilter
