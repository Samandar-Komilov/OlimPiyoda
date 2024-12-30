from drf_spectacular.utils import OpenApiExample, OpenApiResponse, extend_schema
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.users.api_endpoints.Login.serializers import UserLoginSerializer


class LoginAPIView(TokenObtainPairView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny,)

    @extend_schema(
        tags=["Authentication"],
        summary="Login user",
        description="Login user with email and password",
        request=UserLoginSerializer,
        responses={
            200: OpenApiResponse(  # Changed from 201 to 200 as login is not creating a resource
                description="User successfully logged in",
                examples=[
                    OpenApiExample(
                        "Success",
                        value={
                            "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
                            "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
                        },
                    )
                ],
            ),
            400: OpenApiResponse(
                description="Invalid input",
                examples=[
                    OpenApiExample(
                        "Validation Error",
                        value={"email": ["This field is required."], "password": ["This field is required."]},
                    )
                ],
            ),
            401: OpenApiResponse(
                description="Authentication failed",
                examples=[
                    OpenApiExample(
                        "Authentication Error",
                        value={"detail": "Invalid credentials"},
                    )
                ],
            ),
        },
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
