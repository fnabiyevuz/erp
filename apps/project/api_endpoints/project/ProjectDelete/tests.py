from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.project.models import Project, Service, ProjectType
from apps.common.tests import basic_auth


class ProjectDestroyAPIViewTestCase(APITestCase):

    def setUp(self):

        # Create a ProjectType instance for testing purposes
        self.project_type = ProjectType.objects.create(name="Test Type")

        self.project = Project.objects.create(name="Test Project", type_id=1, deadline='2023-04-30')
        self.url = reverse('project-delete', args=[self.project.pk])

        self.auth = basic_auth()

    def test_delete_project(self):
        response = self.client.delete(self.url, HTTP_AUTHORIZATION=f"Basic {self.auth}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Project.objects.filter(pk=self.project.pk).exists())
