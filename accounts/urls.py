from django.urls import path, include
from .views import RegisterApiView, LoginApiView, UserApiView
from knox import views as knox_views

urlpatterns = [
    path("api/auth", include("knox.urls")),
    path("api/auth/register", RegisterApiView.as_view()),
    path("api/auth/login", LoginApiView.as_view()),
    path("api/auth/user", UserApiView.as_view()),
    path("api/auth/logout", knox_views.LogoutView.as_view(), name="knox_logout"),
]
