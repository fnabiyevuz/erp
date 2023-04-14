from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from apps.staff.api_endpoints.attendance.AttendanceCreate.serializers import AttendanceCreateSerializer
from apps.staff.models import Attendance
from datetime import datetime, time, date, timedelta


class AttendanceCreateAPIView(CreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceCreateSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        if data['is_absent']:
            pass
        else:
            expected_arrival_time = time(hour=10, minute=0)
            actual_arrival_time = datetime.now().time()

            time_difference = datetime.combine(date.today(), actual_arrival_time) - datetime.combine(date.today(),expected_arrival_time)
            time_difference_without_seconds = str(timedelta(seconds=time_difference.seconds)).split(".")[0]

            data['lated_minutes'] = time_difference_without_seconds
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


__all__ = ["AttendanceCreateAPIView"]
