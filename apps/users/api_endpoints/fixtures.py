import secrets

import pytest
from django.contrib.auth import get_user_model

test_email = secrets.token_hex(8) + "@example.com"
test_password = secrets.token_hex(8)
test_username = secrets.token_hex(8)


@pytest.fixture(scope="module")
def api_client():
    from rest_framework.test import APIClient

    return APIClient()


@pytest.fixture
def test_user(db):
    User = get_user_model()
    return User.objects.create_user(email=test_email, password=test_password, username=test_username)
