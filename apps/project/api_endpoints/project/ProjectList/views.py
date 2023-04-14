from rest_framework.generics import ListAPIView

from apps.project.api_endpoints.project.ProjectCreate.serializers import ProjectSerializer
from apps.project.models import Project


class ProjectListAPIView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


__all__ = ["ProjectListAPIView"]
