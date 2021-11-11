from rest_framework import generics, permissions, views, viewsets
from rest_framework.response import Response
from knox.models import AuthToken

from accounts.models import CustomUser
from .serializers import (
    UserAuthSerializer,
    UserSerializer,
    RegisterSerializer,
    LoginSerializer,
)


class RegisterApiView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )


class LoginApiView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )


class UserAuthApiView(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserAuthSerializer

    def get_object(self):
        return self.request.user


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


class UserByUserTag(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, user_tag):
        user = generics.get_object_or_404(CustomUser.objects.all(), user_tag=user_tag)
        serializedUser = UserSerializer(user)
        return Response(serializedUser.data)
