from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.common.tests import basic_auth
from apps.project.models import Service


class ServiceListAPIViewTestCase(APITestCase):

    def setUp(self):
        self.url = reverse('service-list')
        Service.objects.create(name="Service 1")
        Service.objects.create(name="Service 2")

        self.auth = basic_auth()

    def test_list_services(self):
        response = self.client.get(self.url, HTTP_AUTHORIZATION=f"Basic {self.auth}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], "Service 1")
        self.assertEqual(response.data[1]['name'], "Service 2")
