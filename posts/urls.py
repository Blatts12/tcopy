from django.urls import include, path
from rest_framework import routers

from posts.views import UserPostViewSet

router = routers.DefaultRouter()
router.register(r"posts", UserPostViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
