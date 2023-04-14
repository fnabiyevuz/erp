from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.staff.api_endpoints.staff.StaffCreate.serializers import StaffSerializer
from apps.staff.models import Staff


class StaffCreateAPIView(CreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [IsAuthenticated]


__all__ = ["StaffCreateAPIView"]
