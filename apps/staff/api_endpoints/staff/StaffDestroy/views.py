from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from apps.staff.api_endpoints.staff.StaffCreate.serializers import StaffSerializer
from apps.staff.models import Staff


class StaffDestroyAPIView(DestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [IsAuthenticated]


__all__ = ["StaffDestroyAPIView"]
