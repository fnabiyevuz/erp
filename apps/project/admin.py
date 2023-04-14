from django.contrib import admin

from django.contrib import admin
from .models import Service, ProjectType, Project


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(ProjectType)
class ProjectTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name', 'deadline')
    list_display_links = ('id', 'type')
    list_filter = ('service', 'type')
