from rest_framework import serializers

from apps.staff.models import Staff


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['id', 'position', 'full_name', 'birthday', 'bio']