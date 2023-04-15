from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.common.tests import basic_auth
from apps.inventory.models import Inventory


class InventoryRetrieveUpdateDestroyAPIViewTestCase(APITestCase):

    def setUp(self):
        self.inventory = Inventory.objects.create(name="Test Inventory", quantity=10)
        self.url = reverse('inventory-retrieve-update-destroy', args=[self.inventory.pk])

        self.auth = basic_auth()

    def test_retrieve_inventory(self):
        response = self.client.get(self.url, HTTP_AUTHORIZATION=f"Basic {self.auth}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.inventory.name)
        self.assertEqual(response.data['quantity'], self.inventory.quantity)

    def test_update_inventory(self):
        data = {'name': 'New Name', 'quantity': 10}
        response = self.client.put(self.url, data, HTTP_AUTHORIZATION=f"Basic {self.auth}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.inventory.refresh_from_db()
        self.assertEqual(self.inventory.name, data['name'])
        self.assertEqual(self.inventory.quantity, data['quantity'])

    def test_delete_inventory(self):
        response = self.client.delete(self.url, HTTP_AUTHORIZATION=f"Basic {self.auth}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Inventory.objects.filter(pk=self.inventory.pk).exists())
