from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "email", "password", )

    def create(self, validated_data):
        """Create a new user with encrypted password"""
        return get_user_model().objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Update a user, set password correctly"""
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user
