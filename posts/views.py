from rest_framework import viewsets
from rest_framework import permissions

from posts.models import UserPost
from posts.paginations import FeedPagination
from posts.serializers import UserPostSerializer


class UserPostViewSet(viewsets.ModelViewSet):
    queryset = UserPost.objects.all().order_by("-pub_date")
    serializer_class = UserPostSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = FeedPagination
