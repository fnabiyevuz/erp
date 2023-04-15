from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from apps.common.tests import basic_auth
from apps.staff.models import Position


class PositionListCreateAPIViewTest(APITestCase):
    def setUp(self):
        self.url = reverse('position')
        self.position1 = Position.objects.create(name="Position 1")
        self.position2 = Position.objects.create(name="Position 2")

        self.auth = basic_auth()

    def test_position_list(self):
        response = self.client.get(self.url, HTTP_AUTHORIZATION=f"Basic {self.auth}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["name"], "Position 1")
        self.assertEqual(response.data[1]["name"], "Position 2")

    def test_position_create(self):
        data = {"name": "Position 3"}
        response = self.client.post(self.url, data=data, HTTP_AUTHORIZATION=f"Basic {self.auth}")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Position.objects.count(), 3)
        self.assertEqual(Position.objects.last().name, "Position 3")
