from django.db import models


class StaffType(models.TextChoices):
    STAFF = "Staff"
    INTERN = "Intern"
