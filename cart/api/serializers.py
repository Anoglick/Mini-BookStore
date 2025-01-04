from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from django.contrib.auth.models import User
from .models import Cart, CartItem

from datetime import datetime

class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CartItemSerializer(ModelSerializer):
    user_id = PrimaryKeyRelatedField(source='cart.user', read_only=True)
    cart = CartSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'product_id', 'quantity', 'price', 'cart', 'user_id']