from rest_framework import generics
from rest_framework.exceptions import NotFound

from django.contrib.auth.models import User
from .serializers import UserSerializer


class UserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return User.objects.all()

    def get_object(self):
        try:
            obj = self.get_queryset().get(id=self.kwargs['id'])
        except User.DoesNotExist:
            raise NotFound(detail="Пользователь не найден")
        return obj