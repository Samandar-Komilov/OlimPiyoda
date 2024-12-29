from drf_spectacular.utils import OpenApiExample, OpenApiResponse, extend_schema
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from apps.users.api_endpoints.Profile.serializers import ProfileSerializer
from apps.users.models import User


class ProfileAPIView(RetrieveAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    @extend_schema(
        tags=["Authentication"],
        summary="Get user profile",
        description="Get user profile information",
        responses={
            200: OpenApiResponse(
                description="User profile successfully retrieved",
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
                            "region": "Tashkent",
                            "district": "Chilonzor",
                            "address": "Chilonzor",
                            "is_verified": False,
                        },
                    )
                ],
            ),
            403: OpenApiResponse(description="You are not authenticated"),
        },
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
