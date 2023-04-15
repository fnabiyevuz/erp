from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.common.tests import basic_auth
from apps.project.models import ProjectType, Service


class ProjectTypeListAPIViewTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('project-create')

        # Create a Service instance for testing purposes
        self.service = Service.objects.create(name="Test Service")

        # Create a ProjectType instance for testing purposes
        self.project_type = ProjectType.objects.create(name="Test Type")

        self.auth = basic_auth()

    def test_create_project(self):
        data = {
            "service": [self.service.pk],
            "type": self.project_type.pk,
            "name": "Test Project",
            "deadline": "2023-04-16"
        }
        response = self.client.post(self.url, data, HTTP_AUTHORIZATION=f"Basic {self.auth}")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        project = response.data
        self.assertEqual(project["service"][0], self.service.pk)
        self.assertEqual(project["type"], self.project_type.pk)
        self.assertEqual(project["name"], data["name"])
        self.assertEqual(project["deadline"], data["deadline"])
