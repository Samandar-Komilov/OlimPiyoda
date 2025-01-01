from django.contrib.auth import authenticate
from rest_framework import exceptions, serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserLoginSerializer(TokenObtainPairSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    # Override the username_field
    username_field = "email"

    default_error_messages = {
        "no_active_account": "No active account found with the given credentials",
        "invalid_credentials": "Invalid credentials",
    }

    def validate(self, attrs):
        authenticate_kwargs = {
            "email": attrs["email"],
            "password": attrs["password"],
        }
        try:
            authenticate_kwargs["request"] = self.context["request"]
        except KeyError:
            pass

        user = authenticate(**authenticate_kwargs)

        if user is None:
            raise exceptions.AuthenticationFailed(
                self.error_messages["invalid_credentials"],
                "invalid_credentials",
            )

        if not user.is_active:
            raise exceptions.AuthenticationFailed(
                self.error_messages["no_active_account"],
                "no_active_account",
            )

        refresh = self.get_token(user)

        data = {
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
        }

        return data
