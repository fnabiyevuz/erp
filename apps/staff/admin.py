from django.contrib import admin
from .models import Position, Staff, Attendance


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'position', 'birthday')
    list_display_links = ('id', 'full_name')
    list_filter = ('position',)


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'staff', 'lated_minutes', 'is_absent')
    list_display_links = ('id', 'staff')
    list_filter = ('is_absent',)
