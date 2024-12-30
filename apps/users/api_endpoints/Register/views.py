import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from drf_spectacular.utils import OpenApiExample, OpenApiResponse, extend_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.users.api_endpoints.Register.serializers import UserRegisterSerializer
from apps.users.tasks import send_confirm_email

User = get_user_model()


class RegisterAPIView(GenericAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = (AllowAny,)

    @extend_schema(
        tags=["Authentication"],
        summary="Register a new user",
        description="Create a new user account with email and password",
        request=UserRegisterSerializer,
        responses={
            201: OpenApiResponse(
                description="User successfully registered",
                examples=[
                    OpenApiExample(
                        "Success",
                        value={
                            "email": "user@example.com",
                            "first_name": "John",
                            "last_name": "Doe",
                            "username": "johndoe",
                            "phone": "+998770007711",
                            "gender": "male",
                        },
                    )
                ],
            ),
            400: OpenApiResponse(
                description="Invalid input",
                examples=[
                    OpenApiExample(
                        "Validation Error",
                        value={"email": ["This field is required."], "password": ["Passwords don't match"]},
                    )
                ],
            ),
        },
    )
    def post(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            token = jwt.encode({"email": user.email}, settings.SECRET_KEY, algorithm="HS256")
            send_confirm_email.delay(user.email, token)

            return Response(
                {
                    "message": "Registration successful. Please check your email for verification.",
                    "user": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
