from rest_framework import serializers

from apps.users.models import User

# from apps.users.tests.factories import UserFactory


class UserRegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("email", "password", "password_confirm", "first_name", "last_name", "username", "phone", "gender")
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, attrs):
        if attrs["password"] != attrs.pop("password_confirm"):
            raise serializers.ValidationError("Passwords don't match")
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


# class TestUserRegisterSerializer:
#     def test_create_user(self, db):
#         serializer = UserRegisterSerializer(data={"email": "test@example.com", "password": "test123", "password_confirm": "test123"})
#         assert serializer.is_valid()
#         user = serializer.save()
#         assert user.email == "test@example.com"

#     def test_validate_passwords(self, db):
#         serializer = UserRegisterSerializer(data={"email": "test@example.com", "password": "test123", "password_confirm": "test111"})
#         assert not serializer.is_valid()
#         assert serializer.errors["password_confirm"][0] == "Passwords don't match"
