from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

class EmailRegisterSerializer(RegisterSerializer):
    username = None
    email = serializers.EmailField(required=True)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data.pop("username", None)
        return data

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

class RefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()