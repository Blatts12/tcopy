from rest_framework import serializers
from accounts.models import CustomUser
from accounts.serializers import UserSerializer
from posts.models import UserPost


class UserPostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        source="CustomUser", queryset=CustomUser.objects.all(), write_only=True
    )

    class Meta:
        model = UserPost
        fields = "__all__"

    def create(self, validated_data):
        userPost = UserPost.objects.create(
            content=validated_data["content"], author_id=validated_data["CustomUser"].id
        )

        return userPost
