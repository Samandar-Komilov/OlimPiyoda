from rest_framework import serializers


class RegisterConfirmSerializer(serializers.Serializer):
    token = serializers.CharField()
