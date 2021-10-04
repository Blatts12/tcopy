from rest_framework import serializers

from posts.models import UserPost


class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPost
        fields = "__all__"
