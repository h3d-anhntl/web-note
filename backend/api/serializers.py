from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fiels = ["id", "username", "password"]
        extra_kwargs = {"password": {"wrie_only": True}}
        
    def create(self, validated_data):
        user = User.object.create_user(**validated_data)
        return user