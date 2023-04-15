from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from apps.common.tests import basic_auth
from apps.project.models import Project, ProjectType


class ProjectListAPIViewTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('project-list')

        # Create a ProjectType instance for testing purposes
        self.project_type1 = ProjectType.objects.create(name="Test Type 1")
        self.project_type2 = ProjectType.objects.create(name="Test Type 2")

        self.project1 = Project.objects.create(name='Project 1', type=self.project_type1, deadline="2023-07-30")
        self.project2 = Project.objects.create(name='Project 2', type=self.project_type2, deadline="2023-07-30")

        self.auth = basic_auth()

    def test_get_project_list(self):
        response = self.client.get(self.url, HTTP_AUTHORIZATION=f"Basic {self.auth}")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], self.project1.name)
        self.assertEqual(response.data[1]['name'], self.project2.name)
        self.assertEqual(response.data[0]['deadline'], self.project1.deadline)
        self.assertEqual(response.data[1]['deadline'], self.project2.deadline)
        self.assertEqual(response.data[0]['type'], self.project1.type.name)
        self.assertEqual(response.data[1]['type'], self.project2.type.name)
