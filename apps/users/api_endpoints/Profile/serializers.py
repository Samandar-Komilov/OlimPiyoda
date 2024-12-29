from rest_framework import serializers

from apps.users.models import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "username",
            "phone",
            "gender",
            "region",
            "district",
            "address",
            "is_verified",
        )
