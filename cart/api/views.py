from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import CartItem
from .serializers import CartItemSerializer 


class CartRead(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return CartItem.objects.filter(cart__user_id=self.request.user)
        else:
            session_key = self.request.session.session_key
            if session_key:
                return CartItem.objects.filter(cart__session_key=session_key)
            else:
                cart = CartItem.objects.create(session_key=self.request.session.session_key)
                self.request.session.modified = True
                return CartItem.objects.filter(cart=cart)

class CartUpdate(generics.UpdateAPIView):
    serializer_class = CartItemSerializer

    def get_object(self, product_id):
        try:
            cart_item = CartItem.objects.filter(cart__user_id=self.request.user.id, product_id=product_id).first()
            if not cart_item:
                raise ValueError("Cart item not found.")
            return cart_item
        except Exception as e:
            print(f"Error retrieving cart item: {e}")
            return None

    def update(self, request, *args, **kwargs):
        product_id = kwargs.get('product_id')
        cart_item = self.get_object(product_id)

        if cart_item is not None:
            action = request.data.get('action')
            if action == 'increment':
                cart_item.quantity += 1
            
            elif action == 'decrement':
                if cart_item.quantity > 1:
                    cart_item.quantity -= 1
                
                else:
                    cart_item.delete()
                    return Response({'quantity': 0}, status=200)

            cart_item.save()
            return Response(CartItemSerializer(cart_item).data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Cart item not found."}, status=status.HTTP_404_NOT_FOUND)
