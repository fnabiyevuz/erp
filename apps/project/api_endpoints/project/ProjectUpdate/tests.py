from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.common.tests import basic_auth
from apps.project.models import Project, ProjectType


class ProjectUpdateAPIViewTestCase(APITestCase):
    def setUp(self):

        # Create a ProjectType instance for testing purposes
        self.project_type = ProjectType.objects.create(name="Test Type 1")

        self.project = Project.objects.create(name='Test Project', type=self.project_type, deadline='2023-04-30')
        self.url = reverse('project-update', kwargs={'pk': self.project.pk})
        self.valid_data = {
            'name': 'Updated Project Name',
            'deadline': '2023-05-31'
        }

        self.auth = basic_auth()

    def test_update_data(self):
        response = self.client.patch(self.url, data=self.valid_data, HTTP_AUTHORIZATION=f"Basic {self.auth}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.valid_data['name'])
        self.assertEqual(response.data['deadline'], self.valid_data['deadline'])

