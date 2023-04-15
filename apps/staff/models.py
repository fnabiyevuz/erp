from django.db import models
from apps.common.models import BaseModel
from apps.staff.choices import StaffType
from django.utils.translation import gettext as _


class Position(BaseModel):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Position"
        verbose_name_plural = "Positions"


class Staff(BaseModel):
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=100)
    birthday = models.DateField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    type = models.CharField(verbose_name=_("Staff type"), max_length=25, choices=StaffType.choices,
                            default=StaffType.STAFF)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staff"


class Attendance(BaseModel):
    staff = models.ForeignKey('staff.Staff', on_delete=models.CASCADE, related_name='staff_attendance')
    lated_minutes = models.DurationField(null=True, blank=True)
    is_absent = models.BooleanField(default=False)

    def __str__(self):
        return self.staff.full_name

    class Meta:
        verbose_name = "Attandance"
        verbose_name_plural = "Attandances"
        unique_together = ('staff', 'created_at')
