from rest_framework import serializers

from apps.project.api_endpoints.project_type.ProjectTypeList.serializers import ProjectTypeSerializer
from apps.project.api_endpoints.service.ServiceList.serializers import ServiceSerializer
from apps.project.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True)
    type = ProjectTypeSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'service', 'type', 'name', 'deadline')
