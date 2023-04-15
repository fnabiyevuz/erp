from rest_framework import status
from rest_framework.test import APITestCase
from apps.staff.models import Position
from django.urls import reverse

from apps.common.tests import basic_auth

class PositionRetrieveUpdateDestroyAPIViewTest(APITestCase):
    def setUp(self):
        self.position = Position.objects.create(name='Position 1')

        self.auth = basic_auth()

    def test_retrieve_position(self):
        url = reverse('position-retrieve-update-destroy', kwargs={'pk': self.position.pk})
        response = self.client.get(url, HTTP_AUTHORIZATION=f"Basic {self.auth}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Position 1')

    def test_update_position(self):
        url = reverse('position-retrieve-update-destroy', kwargs={'pk': self.position.pk})
        data = {'name': 'Updated Position'}
        response = self.client.put(url, data, format='json', HTTP_AUTHORIZATION=f"Basic {self.auth}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Position')

    def test_delete_position(self):
        url = reverse('position-retrieve-update-destroy', kwargs={'pk': self.position.pk})
        response = self.client.delete(url, HTTP_AUTHORIZATION=f"Basic {self.auth}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Position.objects.filter(pk=self.position.pk).exists())
