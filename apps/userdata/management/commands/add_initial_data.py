# coding=utf-8
from django.core.management.base import BaseCommand
from django.utils import timezone
from dateutil.relativedelta import relativedelta

from userdata.models import Presence, Steps, Sleep


class Command(BaseCommand):
    help = 'Добавить тестые данные'

    def handle(self, *args, **options):
        now_time = timezone.now()
        past_time = now_time - relativedelta(hours=1)
        future_time = now_time + relativedelta(hours=1)

        Presence.objects.create(
            time_start=past_time,
            time_end=now_time,
            point='POINT(39.844923 59.214524)'
        )
        Presence.objects.create(
            time_start=now_time,
            time_end=future_time,
            point='POINT(39.813997 59.202766)'
        )
        Steps.objects.create(
            time_start=past_time,
            time_end=now_time,
            count=100
        )
        Steps.objects.create(
            time_start=now_time,
            time_end=future_time,
            count=200
        )
        Sleep.objects.create(
            time_start=past_time - relativedelta(hours=16),
            time_end=now_time - relativedelta(hours=32)
        )
        Sleep.objects.create(
            time_start=now_time - relativedelta(hours=40),
            time_end=future_time - relativedelta(hours=8)
        )
