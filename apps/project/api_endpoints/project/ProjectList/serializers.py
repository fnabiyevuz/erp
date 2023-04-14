from rest_framework import serializers

from apps.project.models import Project


class ProjectListSerializer(serializers.ModelSerializer):
    service = serializers.StringRelatedField(many=True)
    type = serializers.StringRelatedField()

    class Meta:
        model = Project
        fields = ('id', 'service', 'type', 'name', 'deadline')
