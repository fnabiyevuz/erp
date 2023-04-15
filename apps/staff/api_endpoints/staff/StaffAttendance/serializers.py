from rest_framework import serializers

from apps.staff.models import Attendance


class AttendanceListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendance
        fields = ('id', 'is_absent', 'lated_minutes', 'created_at')