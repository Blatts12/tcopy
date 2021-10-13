from rest_framework import serializers
from django.contrib.auth.models import User

from posts.models import UserPost


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "is_staff",
            "is_active",
            "date_joined",
        ]


class UserPostSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = UserPost
        fields = "__all__"
        read_only_fields = ["author"]
