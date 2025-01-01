from django.urls import path

from apps.olympiads.api_endpoints import OlympiadList

urlpatterns = [
    path("", OlympiadList.OlympiadListAPIView.as_view(), name="olympiad-list"),
]
