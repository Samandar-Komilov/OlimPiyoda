import secrets

import pytest
from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class UserManagerTests(TestCase):
    def test_create_user(self):
        email = secrets.token_hex(8) + "@example.com"
        password = secrets.token_hex(8)
        user = User.objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertEqual(user.check_password(password), True)
        self.assertEqual(user.is_active, True)
        self.assertEqual(user.is_staff, False)
        self.assertEqual(user.is_superuser, False)

        # username is None for the AbstractUser option
        # username does not exist for the AbstractBaseUser option
        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass

        # Test invalid user creation (empty email, missing parameters)
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(ValueError):
            User.objects.create_user(email="")
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password=password)

    def test_create_superuser(self):
        email = secrets.token_hex(8) + "@example.com"
        password = secrets.token_hex(8)
        user = User.objects.create_superuser(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertEqual(user.check_password(password), True)
        self.assertEqual(user.is_active, True)
        self.assertEqual(user.is_staff, True)
        self.assertEqual(user.is_superuser, True)

        # username is None for the AbstractUser option
        # username does not exist for the AbstractBaseUser option
        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass

        # Test invalid superuser creation (empty email, missing parameters)
        with self.assertRaises(TypeError):
            User.objects.create_superuser()
        with self.assertRaises(ValueError):
            User.objects.create_superuser(email="")
        with self.assertRaises(ValueError):
            User.objects.create_superuser(email="", password=password)

    def test_create_staffuser(self):
        email = secrets.token_hex(8) + "@example.com"
        password = secrets.token_hex(8)
        user = User.objects.create_staffuser(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertEqual(user.check_password(password), True)
        self.assertEqual(user.is_active, True)
        self.assertEqual(user.is_staff, True)
        self.assertEqual(user.is_superuser, False)

        # username is None for the AbstractUser option
        # username does not exist for the AbstractBaseUser option
        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass

        # Test invalid staffuser creation (empty email, missing parameters)
        with self.assertRaises(TypeError):
            User.objects.create_staffuser()
        with self.assertRaises(ValueError):
            User.objects.create_staffuser(email="")
        with self.assertRaises(ValueError):
            User.objects.create_staffuser(email="", password=password)
