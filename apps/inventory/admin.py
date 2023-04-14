from django.contrib import admin
from .models import Inventory


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'quantity')
    list_display_links = ('id', 'name')
