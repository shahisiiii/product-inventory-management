"""User serializers for authentication."""

from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user data."""

    class Meta:
        model = User
        fields = ["id", "email", "username", "role", "created_at"]
        read_only_fields = ["id", "created_at"]


class LoginSerializer(serializers.Serializer):
    """Serializer for user login."""

    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        """Validate user credentials."""
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            user = authenticate(
                request=self.context.get("request"), username=email, password=password
            )

            if not user:
                raise serializers.ValidationError(
                    "Invalid email or password.", code="authorization"
                )

            if not user.is_active:
                raise serializers.ValidationError(
                    "User account is disabled.", code="authorization"
                )

            attrs["user"] = user
            return attrs

        raise serializers.ValidationError(
            'Must include "email" and "password".', code="authorization"
        )
