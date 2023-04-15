from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.common.tests import basic_auth
from apps.staff.models import Staff


class StaffUpdateAPIViewTestCase(APITestCase):
    def setUp(self):
        self.staff = Staff.objects.create(full_name="John Doe")

        self.auth = basic_auth()

    def test_staff_update(self):
        url = reverse('staff-update', kwargs={'pk': self.staff.pk})
        data = {'full_name': 'Jane Doe'}
        response = self.client.put(url, data, HTTP_AUTHORIZATION=f"Basic {self.auth}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.staff.refresh_from_db()
        self.assertEqual(self.staff.full_name, data['full_name'])
