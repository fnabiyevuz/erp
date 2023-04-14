from rest_framework.generics import ListAPIView

from apps.staff.api_endpoints.attendance.AttendanceList.serializers import AttendanceSerializer
from apps.staff.models import Attendance


class AttendanceListAPIView(ListAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


__all__ = ["AttendanceListAPIView"]
