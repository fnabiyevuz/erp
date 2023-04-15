from datetime import timedelta

from rest_framework import status
from rest_framework.test import APITestCase

from apps.common.tests import basic_auth
from apps.staff.choices import StaffType
from apps.staff.models import Attendance, Staff, Position
from django.urls import reverse


class AttendanceListAPIViewTest(APITestCase):
    def setUp(self):
        # Create a Position instance for testing purposes
        self.position = Position.objects.create(name="Position 1")

        # Create a Staff instance for testing purposes
        self.staff1 = Staff.objects.create(position=self.position, full_name='Jack Jack1', type=StaffType.STAFF,
                                           bio="Bio")
        self.staff2 = Staff.objects.create(position=self.position, full_name='Jack Jack2', type=StaffType.STAFF,
                                           bio="Bio")

        # Create test data
        Attendance.objects.create(
            staff=self.staff1,
            lated_minutes=timedelta(minutes=5),
            is_absent=False
        )
        Attendance.objects.create(
            staff=self.staff2,
            lated_minutes=None,
            is_absent=True
        )

        self.auth = basic_auth()

    def test_attendance_list(self):
        url = reverse('attendance-list')
        response = self.client.get(url, HTTP_AUTHORIZATION=f"Basic {self.auth}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["staff"]['id'], self.staff1.id)
        self.assertEqual(response.data[0]["lated_minutes"], "00:05:00")
        self.assertEqual(response.data[0]["is_absent"], False)
        self.assertEqual(response.data[1]["staff"]['id'], self.staff2.id)
        self.assertEqual(response.data[1]["lated_minutes"], None)
        self.assertEqual(response.data[1]["is_absent"], True)
