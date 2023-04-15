from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.common.tests import basic_auth
from apps.staff.choices import StaffType
from apps.staff.models import Staff, Position


class StaffCreateAPIViewTest(APITestCase):
    def setUp(self):
        self.position = Position.objects.create(name='Backend developer')

        self.test_data = {
            'position': self.position.id,
            'full_name': 'John Doe',
            'birthday': '1990-01-01',
            'bio': 'Some bio',
            'type': StaffType.STAFF
        }

        self.url = reverse('staff-create')
        self.auth = basic_auth()

    def test_create_staff(self):
        response = self.client.post(self.url, self.test_data, format='json', HTTP_AUTHORIZATION=f"Basic {self.auth}")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
