from rest_framework.generics import ListAPIView

from apps.project.api_endpoints.project.ProjectList.serializers import ProjectListSerializer
from apps.project.models import Project


class ProjectListAPIView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer


__all__ = ["ProjectListAPIView"]
