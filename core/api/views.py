from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from .permissions import IsUser, isAdminOrModerator
from cart.api.models import Cart, CartItem
from ..general.models import Category, BooksItems
from .serializers import AddToCartSerializer, ProductSerializer, CategorySerializer

from django.shortcuts import get_object_or_404

class Categories(generics.ListCreateAPIView):
    queryset = Category.objects.all().order_by('title')
    serializer_class = CategorySerializer

class OneCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class APIProductItem(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        if category_id is not None:
            return BooksItems.objects.filter(category_id=category_id).order_by('title')
        return BooksItems.objects.select_related('category').all().order_by('title')

class ProductItemByID(generics.RetrieveUpdateAPIView):
    queryset = BooksItems.objects.all()
    serializer_class = ProductSerializer
        
class AddToCartAPIView(APIView):
    def post(self, request, product_id):
        serializer = AddToCartSerializer(data=request.data)
        if serializer.is_valid():
            quantity = serializer.validated_data['quantity']
            user = request.user if request.user.is_authenticated else None
            session_key = request.session.session_key if not user else None
            
            if user:
                user_cart, created = Cart.objects.get_or_create(user_id=user)
            else:
                if not session_key:
                    request.session.create()
                    session_key = request.session.session_key

                user_cart, created = Cart.objects.get_or_create(session_key=session_key)

            product = get_object_or_404(BooksItems, pk=product_id)
            CartItem.objects.create(product_id=product, quantity=quantity, price=product.price, cart=user_cart)
            
            return Response({'message': 'Товар успешно добавлен в корзину'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)