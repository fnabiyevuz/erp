from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.common.tests import basic_auth
from apps.staff.models import Staff, Position


class StaffListAPIViewTestCase(APITestCase):
    def setUp(self):
        self.position1 = Position.objects.create(name='Frontend')
        self.position2 = Position.objects.create(name='Backend')

        self.staff1 = Staff.objects.create(full_name='John Doe', position=self.position1)
        self.staff2 = Staff.objects.create(full_name='Jane Doe', position=self.position1)
        self.staff3 = Staff.objects.create(full_name='Alice Smith', position=self.position2)

        self.auth = basic_auth()

    def test_filter_by_position(self):
        url = reverse('staff-list')
        response = self.client.get(url, {'position': self.position1.id}, HTTP_AUTHORIZATION=f"Basic {self.auth}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['full_name'], 'John Doe')
        self.assertEqual(response.data[1]['full_name'], 'Jane Doe')

    def test_search_by_full_name(self):
        url = reverse('staff-list')
        response = self.client.get(url, {'search': 'Doe'}, HTTP_AUTHORIZATION=f"Basic {self.auth}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['full_name'], 'John Doe')
        self.assertEqual(response.data[1]['full_name'], 'Jane Doe')

    def test_filter_and_search(self):
        url = reverse('staff-list')
        response = self.client.get(url, {'position': self.position1.id, 'search': 'Doe'},
                                   HTTP_AUTHORIZATION=f"Basic {self.auth}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['full_name'], 'John Doe')
        self.assertEqual(response.data[1]['full_name'], 'Jane Doe')
