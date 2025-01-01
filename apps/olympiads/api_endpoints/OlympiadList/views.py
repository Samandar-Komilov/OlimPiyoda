from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.olympiads.api_endpoints.OlympiadList.serializers import OlympiadListSerializer
from apps.olympiads.models import Olympiad


@extend_schema(tags=["Olympiads"], summary="Olympiad List")
class OlympiadListAPIView(ListAPIView):
    queryset = Olympiad.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = OlympiadListSerializer
