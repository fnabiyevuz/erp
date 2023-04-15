from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.project.models import Project, Service, ProjectType
from apps.common.tests import basic_auth


class ProjectDestroyAPIViewTestCase(APITestCase):

    def setUp(self):
        # Create a ProjectType instance for testing purposes
        self.project_type = ProjectType.objects.create(name="Test Type")

        self.project = Project.objects.create(name="Test Project", type=self.project_type, deadline='2023-07-30')
        self.url = reverse('project-detail', args=[self.project.pk])

        self.auth = basic_auth()

    def test_retrieve_inventory(self):
        response = self.client.get(self.url, HTTP_AUTHORIZATION=f"Basic {self.auth}")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.project.name)
        self.assertEqual(response.data['type'], self.project.type.id)
        self.assertEqual(response.data['deadline'], self.project.deadline)
