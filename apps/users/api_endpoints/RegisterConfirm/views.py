import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from drf_spectacular.utils import OpenApiExample, OpenApiResponse, extend_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.api_endpoints.RegisterConfirm.serializers import RegisterConfirmSerializer

User = get_user_model()


class RegisterConfirmAPIView(GenericAPIView):
    serializer_class = RegisterConfirmSerializer
    permission_classes = [
        AllowAny,
    ]

    @extend_schema(
        tags=["Authentication"],
        responses={
            status.HTTP_200_OK: {"description": "Email confirmed successfully"},
            status.HTTP_400_BAD_REQUEST: {"description": "Token has expired or is invalid"},
        },
    )
    def get(self, request, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            print(">>>", payload)
            user = User.objects.get(email=payload["email"])
            print("DEBUG:::", payload, user)
            user.is_verified = True
            user.is_active = True
            user.save()
            return Response({"message": "Email confirmed successfully"}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError:
            return Response({"error": "Token has expired"}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.InvalidTokenError:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
