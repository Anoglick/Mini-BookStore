from rest_framework.serializers import ModelSerializer, DateField
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'last_login']

    
