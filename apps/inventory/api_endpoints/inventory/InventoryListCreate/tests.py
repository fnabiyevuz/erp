from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.common.tests import basic_auth
from apps.inventory.models import Inventory


class InventoryListCreateAPIViewTestCase(APITestCase):

    def setUp(self):
        self.inventory1 = Inventory.objects.create(name="Item 1", quantity=10)
        self.inventory2 = Inventory.objects.create(name="Item 2", quantity=5)
        self.url = reverse('inventory')

        self.auth = basic_auth()

    def test_get_inventory_list(self):
        response = self.client.get(self.url, HTTP_AUTHORIZATION=f"Basic {self.auth}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], self.inventory1.name)
        self.assertEqual(response.data[0]['quantity'], self.inventory1.quantity)
        self.assertEqual(response.data[1]['name'], self.inventory2.name)
        self.assertEqual(response.data[1]['quantity'], self.inventory2.quantity)

    def test_create_inventory(self):
        data = {'name': 'New Item', 'quantity': 3}
        response = self.client.post(self.url, data, HTTP_AUTHORIZATION=f"Basic {self.auth}")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Inventory.objects.count(), 3)
        inventory = Inventory.objects.get(name='New Item')
        self.assertEqual(inventory.quantity, 3)
