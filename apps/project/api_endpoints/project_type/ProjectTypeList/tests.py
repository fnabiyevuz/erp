from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.common.tests import basic_auth
from apps.project.models import ProjectType


class ProjectTypeListAPIViewTestCase(APITestCase):

    def setUp(self):
        self.url = reverse('project-type-list')
        ProjectType.objects.create(name="ProjectType 1")
        ProjectType.objects.create(name="ProjectType 2")

        self.auth = basic_auth()

    def test_list_services(self):
        response = self.client.get(self.url, HTTP_AUTHORIZATION=f"Basic {self.auth}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], "ProjectType 1")
        self.assertEqual(response.data[1]['name'], "ProjectType 2")
