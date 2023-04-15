from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.common.tests import basic_auth
from apps.event.models import Event


class EventRetrieveUpdateDestroyAPIViewTestCase(APITestCase):

    def setUp(self):
        self.event = Event.objects.create(name="Test Event", description="Test description",
                                          schedule="2023-04-15T12:00:00Z")
        self.url = reverse('event-retrieve-update-destroy', args=[self.event.pk])

        self.auth = basic_auth()

    def test_retrieve_event(self):
        response = self.client.get(self.url, HTTP_AUTHORIZATION=f"Basic {self.auth}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.event.name)
        self.assertEqual(response.data['description'], self.event.description)
        # self.assertEqual(response.data['schedule'], self.event.schedule.isoformat())

    def test_update_event(self):
        data = {'name': 'New Name', 'description': 'New description', 'schedule': '2023-04-16T12:00:00Z'}
        response = self.client.put(self.url, data, HTTP_AUTHORIZATION=f"Basic {self.auth}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.event.refresh_from_db()
        self.assertEqual(self.event.name, data['name'])
        self.assertEqual(self.event.description, data['description'])
        # self.assertEqual(self.event.schedule.isoformat(), data['schedule'])

    def test_delete_event(self):
        response = self.client.delete(self.url, HTTP_AUTHORIZATION=f"Basic {self.auth}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Event.objects.filter(pk=self.event.pk).exists())
