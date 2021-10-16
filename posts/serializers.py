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
    author = UserSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        source="User", queryset=User.objects.all(), write_only=True
    )

    class Meta:
        model = UserPost
        fields = "__all__"

    def create(self, validated_data):
        userPost = UserPost.objects.create(
            content=validated_data["content"], author_id=validated_data["User"].id
        )

        return userPost
