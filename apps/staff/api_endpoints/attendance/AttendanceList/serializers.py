from rest_framework import serializers

from apps.staff.api_endpoints.staff.StaffCreate.serializers import StaffSerializer
from apps.staff.models import Attendance


class AttendanceSerializer(serializers.ModelSerializer):
    staff = StaffSerializer(read_only=True)

    class Meta:
        model = Attendance
        fields = ['id', 'staff', 'lated_minutes', 'is_absent']
