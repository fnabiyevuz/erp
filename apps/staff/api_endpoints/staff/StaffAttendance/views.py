from rest_framework.generics import ListAPIView, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from apps.staff.models import Attendance, Staff
from apps.staff.api_endpoints.staff.StaffAttendance.serializers import AttendanceListSerializer


class StaffAttendanceListAPIView(ListAPIView):
    serializer_class = AttendanceListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = {
            'is_absent': ['exact'],
            'lated_minutes': ['gte', 'lte'],
        }

    def get_queryset(self):
        staff_id = self.kwargs.get('pk')

        staff = get_object_or_404(Staff.objects.all(), id=staff_id)
        staff_attendance = Attendance.objects.filter(staff=staff)

        return staff_attendance


__all__ = ['StaffAttendanceListAPIView']
