from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializados de usuário.
    """
    class Meta:
        model = User
        depth = 1
        fields = [
            'email',
            'username',
            'password',
            'first_name',
            'last_name'
            ]
