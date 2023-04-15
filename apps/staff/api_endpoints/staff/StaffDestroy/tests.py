from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.common.tests import basic_auth, login_user
from apps.staff.models import Staff
from apps.users.models import User


class StaffDestroyAPIViewTestCase(APITestCase):
    def setUp(self):
        self.staff = Staff.objects.create(full_name='John Doe')
        self.url = reverse('staff-delete', kwargs={'pk': self.staff.pk})

        self.auth = basic_auth()

    def test_delete_staff_with_authenticated_user(self):
        """
        Ensure that an authenticated user can delete a staff object
        """
        user = User.objects.create(username='root', password='root')
        self.client.force_authenticate(user=user)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_staff_with_unauthenticated_user(self):
        """
        Ensure that an unauthenticated user cannot delete a staff object
        """
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
