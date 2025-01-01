import pytest
from django.urls import reverse
from rest_framework import status

from apps.users.api_endpoints.fixtures import test_password


@pytest.mark.django_db
class TestLoginAPI:
    def test_successful_login(self, api_client, test_user):
        url = reverse("login")
        response = api_client.post(url, {"email": test_user.email, "password": test_password})

        assert response.status_code == 200

    def test_wrong_password(self, api_client, test_user):
        url = reverse("login")
        data = {"email": test_user.email, "password": test_password + "wrong"}

        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_nonexistent_user(self, api_client, test_user):
        url = reverse("login")
        data = {"email": test_user.email + "wrong", "password": test_password}

        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
