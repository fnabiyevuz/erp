from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.common.tests import basic_auth
from apps.staff.models import Staff
from apps.staff.api_endpoints.staff.StaffCreate.serializers import StaffSerializer


class StaffRetrieveAPIViewTestCase(APITestCase):
    def setUp(self):
        self.staff = Staff.objects.create(full_name="John Doe")
        self.url = reverse('staff-detail', kwargs={'pk': self.staff.pk})

        self.auth = basic_auth()

    def test_retrieve_staff(self):
        response = self.client.get(self.url, HTTP_AUTHORIZATION=f"Basic {self.auth}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = StaffSerializer(self.staff).data
        self.assertEqual(response.data, serializer_data)

    def test_retrieve_nonexistent_staff(self):
        url = reverse('staff-detail', kwargs={'pk': 999})
        response = self.client.get(url, HTTP_AUTHORIZATION=f"Basic {self.auth}")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
