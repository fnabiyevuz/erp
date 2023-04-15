from datetime import timedelta

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from apps.common.tests import basic_auth
from apps.staff.models import Staff, Attendance
from apps.staff.api_endpoints.staff.StaffAttendance.serializers import AttendanceListSerializer


class StaffAttendanceListAPIViewTestCase(APITestCase):
    def setUp(self):
        self.staff = Staff.objects.create(full_name='John Doe')
        self.attendance1 = Attendance.objects.create(staff=self.staff, is_absent=True)
        self.attendance2 = Attendance.objects.create(staff=self.staff, lated_minutes=timedelta(minutes=30))

        self.auth = basic_auth()

    def test_staff_attendance_list(self):
        url = reverse('staff-attendance', args=[self.staff.id])
        response = self.client.get(url, HTTP_AUTHORIZATION=f"Basic {self.auth}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        expected_data = AttendanceListSerializer([self.attendance1, self.attendance2], many=True).data
        self.assertEqual(response.data, expected_data)
