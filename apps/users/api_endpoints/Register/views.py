from drf_spectacular.utils import OpenApiExample, OpenApiResponse, extend_schema
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from apps.users.api_endpoints.Register.serializers import UserRegisterSerializer


class RegisterAPIView(CreateAPIView):
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
        return super().post(request, *args, **kwargs)
