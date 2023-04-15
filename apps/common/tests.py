import base64

from django.contrib.auth import login, authenticate
from django.test import TestCase
from rest_framework import HTTP_HEADER_ENCODING

from apps.users.models import User


def basic_auth():
    username = "test_username"
    password = "test_password"

    # Create database user. It needs to be created with django set_password function.
    User.objects.create_user(username=username, password=password)

    # Generate base64 credentials string
    credentials = f"{username}:{password}"
    base64_credentials = base64.b64encode(
        credentials.encode(HTTP_HEADER_ENCODING)
    ).decode(HTTP_HEADER_ENCODING)

    return base64_credentials


def login_user(request):
    username = "test_username"
    password = "test_password"

    user = authenticate(username=username, password=password)

    return user
