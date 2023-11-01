from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users import models


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['email', 'chat_id_telegram', 'password']
