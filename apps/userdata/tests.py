# coding: utf-8
from datetime import datetime
from dateutil.relativedelta import relativedelta
from rest_framework.test import APIClient

from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.test import TestCase

from userdata.models import Presence, Steps, Sleep


class UserdataCheckMixin:

    def check_item(self, item, expected):
        for key, value in expected.items():
            value = item[key]
            if isinstance(expected[key], datetime):
                value = parse_datetime(item[key])
            self.assertEqual(value, expected[key])

    def test_get_filtered(self):
        client = APIClient()
        response = client.get(
            '/userdata/{0}/'.format(self.model_url),
            {
                'time_start': self.past_time - relativedelta(minutes=5),
                'time_end': self.now_time + relativedelta(minutes=5)
            },
            format='json'
        )
        resp_body = response.json()
        self.assertEqual(len(resp_body), 2)

        response = client.get(
            '/userdata/{0}/'.format(self.model_url),
            {
                'time_start': self.past_time + relativedelta(minutes=5),
                'time_end': self.now_time + relativedelta(minutes=5)
            },
            format='json'
        )
        resp_body = response.json()
        self.assertEqual(len(resp_body), 1)
        self.assertEqual(resp_body[0]['id'], 2)

        response = client.get(
            '/userdata/{0}/'.format(self.model_url),
            {
                'time_start': self.past_time - relativedelta(minutes=5),
                'time_end': self.now_time - relativedelta(minutes=5)
            },
            format='json'
        )
        resp_body = response.json()
        self.assertEqual(len(resp_body), 1)
        self.assertEqual(resp_body[0]['id'], 1)

        response = client.get(
            '/userdata/{0}/'.format(self.model_url),
            {
                'time_start': self.past_time + relativedelta(minutes=5),
                'time_end': self.now_time - relativedelta(minutes=5)
            },
            format='json'
        )
        resp_body = response.json()
        self.assertEqual(len(resp_body), 0)


class PresenceApiTestCase(UserdataCheckMixin, TestCase):

    model_url = 'presence'

    def setUp(self):
        self.now_time = timezone.now()
        self.past_time = self.now_time - relativedelta(hours=1)
        Presence.objects.create(
            pk=1,
            time_start=self.past_time,
            time_end=self.now_time,
            point='POINT(39.844923 59.214524)'
        )

        self.future_time = self.now_time + relativedelta(hours=1)
        Presence.objects.create(
            pk=2,
            time_start=self.now_time,
            time_end=self.future_time,
            point='POINT(39.813997 59.202766)'
        )

    def test_get_all(self):
        self.assertEqual(Presence.objects.all().count(), 2)

        client = APIClient()
        response = client.get('/userdata/presence/', format='json')
        resp_body = response.json()
        self.assertEqual(len(resp_body), 2)

        presence_1 = [obj for obj in resp_body if obj['id'] == 1][0]
        self.check_item(
            presence_1,
            {
                'time_start': self.past_time,
                'time_end': self.now_time,
                'point': [39.844923, 59.214524]
            }
        )
        presence_2 = [obj for obj in resp_body if obj['id'] == 2][0]
        self.check_item(
            presence_2,
            {
                'time_start': self.now_time,
                'time_end': self.future_time,
                'point': [39.813997, 59.202766]
            }
        )


class StepsApiTestCase(UserdataCheckMixin, TestCase):

    model_url = 'steps'

    def setUp(self):
        self.now_time = timezone.now()
        self.past_time = self.now_time - relativedelta(hours=1)
        Steps.objects.create(
            pk=1,
            time_start=self.past_time,
            time_end=self.now_time,
            count=100
        )

        self.future_time = self.now_time + relativedelta(hours=1)
        Steps.objects.create(
            pk=2,
            time_start=self.now_time,
            time_end=self.future_time,
            count=200
        )

    def test_get_all(self):
        self.assertEqual(Steps.objects.all().count(), 2)

        client = APIClient()
        response = client.get('/userdata/steps/', format='json')
        resp_body = response.json()
        self.assertEqual(len(resp_body), 2)

        steps_1 = [obj for obj in resp_body if obj['id'] == 1][0]
        self.check_item(
            steps_1,
            {
                'time_start': self.past_time,
                'time_end': self.now_time,
                'count': 100
            }
        )
        steps_2 = [obj for obj in resp_body if obj['id'] == 2][0]
        self.check_item(
            steps_2,
            {
                'time_start': self.now_time,
                'time_end': self.future_time,
                'count': 200
            }
        )


class SleepApiTestCase(UserdataCheckMixin, TestCase):

    model_url = 'sleep'

    def setUp(self):
        self.now_time = timezone.now()
        self.past_time = self.now_time - relativedelta(hours=1)
        Sleep.objects.create(
            pk=1,
            time_start=self.past_time,
            time_end=self.now_time
        )

        self.future_time = self.now_time + relativedelta(hours=1)
        Sleep.objects.create(
            pk=2,
            time_start=self.now_time,
            time_end=self.future_time
        )

    def test_get_all(self):
        self.assertEqual(Sleep.objects.all().count(), 2)

        client = APIClient()
        response = client.get('/userdata/sleep/', format='json')
        resp_body = response.json()
        self.assertEqual(len(resp_body), 2)

        sleep_1 = [obj for obj in resp_body if obj['id'] == 1][0]
        self.check_item(
            sleep_1,
            {
                'time_start': self.past_time,
                'time_end': self.now_time
            }
        )
        sleep_2 = [obj for obj in resp_body if obj['id'] == 2][0]
        self.check_item(
            sleep_2,
            {
                'time_start': self.now_time,
                'time_end': self.future_time
            }
        )
