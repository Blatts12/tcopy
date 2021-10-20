from django.urls import include, path
from rest_framework import routers

from posts.views import GlobalFeedViewSet, UserPostViewSet

router = routers.DefaultRouter()
router.register("api/posts", UserPostViewSet, basename="posts")
router.register("api/feed/global", GlobalFeedViewSet, basename="global_feed")

urlpatterns = [
    path("", include(router.urls)),
]
