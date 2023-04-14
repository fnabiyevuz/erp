from django.db import models

from apps.common.models import BaseModel


class Service(BaseModel):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"


class ProjectType(BaseModel):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Types"


class Project(BaseModel):
    service = models.ManyToManyField('project.Service')
    type = models.ForeignKey('project.ProjectType', on_delete=models.CASCADE, related_name='project_type')
    name = models.CharField(max_length=30)
    deadline = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

