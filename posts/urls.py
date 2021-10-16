from django.urls import include, path
from rest_framework import routers

from posts.views import GlobalFeedViewSet, UserPostViewSet

router = routers.DefaultRouter()
router.register("posts", UserPostViewSet, basename="posts")
router.register("feed/global", GlobalFeedViewSet, basename="global_feed")

urlpatterns = [
    path("", include(router.urls)),
]
