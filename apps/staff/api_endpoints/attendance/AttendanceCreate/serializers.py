from rest_framework import serializers

from apps.staff.models import Attendance


class AttendanceCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendance
        fields = ['id', 'staff', 'lated_minutes', 'is_absent']
