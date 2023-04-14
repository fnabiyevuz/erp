from rest_framework.generics import ListAPIView

from apps.project.api_endpoints.project_type.ProjectTypeList.serializers import ProjectTypeSerializer
from apps.project.models import ProjectType


class ProjectTypeListAPIView(ListAPIView):
    queryset = ProjectType.objects.all()
    serializer_class = ProjectTypeSerializer


__all__ = ["ProjectTypeListAPIView"]
