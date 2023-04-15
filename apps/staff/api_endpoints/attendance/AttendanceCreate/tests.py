from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.common.tests import basic_auth
from apps.staff.models import Attendance, Staff


class AttendanceCreateAPIViewTestCase(APITestCase):
    def setUp(self):
        self.staff = Staff.objects.create(full_name='John Doe')

        self.auth = basic_auth()

    def test_create_attendance(self):
        url = reverse('attendance-create')
        data = {'staff': self.staff.id, 'is_absent': False}

        response = self.client.post(url, data, HTTP_AUTHORIZATION=f"Basic {self.auth}")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Attendance.objects.count(), 1)
        self.assertEqual(Attendance.objects.get().staff, self.staff)

    def test_create_absent_attendance(self):
        url = reverse('attendance-create')
        data = {'staff': self.staff.id, 'is_absent': True}

        response = self.client.post(url, data, HTTP_AUTHORIZATION=f"Basic {self.auth}")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Attendance.objects.count(), 1)
        self.assertEqual(Attendance.objects.get().is_absent, True)
