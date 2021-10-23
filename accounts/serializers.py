from rest_framework import serializers
from django.contrib.auth import authenticate

from accounts.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "id",
            "last_login",
            "date_joined",
            "email",
            "user_tag",
            "display_name",
            "is_staff",
        )


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "email", "user_tag", "display_name", "password")
        # extra_kwargs = {"is_staff": {"read_only": True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            validated_data["email"],
            validated_data["password"],
            validated_data["user_tag"],
            validated_data["display_name"],
        )

        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
