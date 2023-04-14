from django.db import models

from apps.common.models import BaseModel


class Inventory(BaseModel):
    name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Inventory"
        verbose_name_plural = "Inventories"
