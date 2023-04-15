import base64

from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from apps.event.models import Event
from apps.event.api_endpoints.event.EventListCreate.serializers import EventSerializer


class EventListCreateAPIViewTest(APITestCase):
    def setUp(self):
        self.url = reverse('event')
        self.event_data = {'name': 'Test Event', 'description': 'This is a test event.', 'schedule': '2023-04-15T10:00:00Z'}

        self.username = 'root'
        self.password = 'root'
        self.client.credentials(
            HTTP_AUTHORIZATION='Basic ' + base64.b64encode(f'{self.username}:{self.password}'.encode()).decode())
    def test_create_event(self):
        response = self.client.post(self.url, self.event_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Event.objects.count(), 1)
        self.assertEqual(Event.objects.get().name, 'Test Event')

    def test_list_events(self):
        Event.objects.create(name='Event 1', description='This is event 1', schedule='2023-04-15T10:00:00Z')
        Event.objects.create(name='Event 2', description='This is event 2', schedule='2023-04-15T11:00:00Z')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = EventSerializer(Event.objects.all(), many=True).data
        self.assertEqual(response.data, expected_data)
