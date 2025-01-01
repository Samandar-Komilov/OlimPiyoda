from rest_framework import serializers

from apps.olympiads.models import Olympiad


class OlympiadListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Olympiad
        fields = (
            "id",
            "title",
            "description",
            "owner",
            "created_at",
            "start_time",
            "end_time",
            "cost",
            "is_active",
            "is_ongoing",
        )
