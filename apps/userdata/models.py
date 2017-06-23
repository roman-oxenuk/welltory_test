# coding: utf-8
from django.db import models
from django.contrib.gis.db.models.fields import PointField


class CommonUserdata(models.Model):
    class Meta:
        abstract = True

    time_start = models.DateTimeField('Время начала')
    time_end = models.DateTimeField('Время конца')


class Sleep(CommonUserdata):
    class Meta:
        verbose_name='Сон'
        verbose_name_plural='Сны'

    def __str__(self):
        return u'{0} --- {1}'.format(
            self.time_start.strftime('%Y-%m-%d %H:%M %Z'),
            self.time_end.strftime('%Y-%m-%d %H:%M %Z')
        )


class Steps(CommonUserdata):
    class Meta:
        verbose_name='Шаги'
        verbose_name_plural='Шаги'

    def __str__(self):
        return u'{0} --- {1} [{2}]'.format(
            self.time_start.strftime('%Y-%m-%d %H:%M %Z'),
            self.time_end.strftime('%Y-%m-%d %H:%M %Z'),
            self.count
        )

    count = models.PositiveIntegerField('Количество шагов')


class Presence(CommonUserdata):
    class Meta:
        verbose_name='Гео-данные'
        verbose_name_plural='Гео-данные'

    def __str__(self):
        return u'{0} --- {1} {2}'.format(
            self.time_start.strftime('%Y-%m-%d %H:%M %Z'),
            self.time_end.strftime('%Y-%m-%d %H:%M %Z'),
            self.point.coords
        )

    point = PointField('Гео-точка')
