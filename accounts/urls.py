from django.urls import path, include
from .views import (
    RegisterApiView,
    LoginApiView,
    UserByUserTag,
    UserViewSet,
    UserAuthApiView,
)
from knox import views as knox_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path("auth", include("knox.urls")),
    path("auth/register", RegisterApiView.as_view()),
    path("auth/login", LoginApiView.as_view()),
    path("auth/user", UserAuthApiView.as_view()),
    path("auth/logout", knox_views.LogoutView.as_view(), name="knox_logout"),
    path("", include(router.urls)),
    path("users/user_tag/<user_tag>", UserByUserTag.as_view()),
]
