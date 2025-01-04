from django.shortcuts import render
from cart.api.models import CartItem

def cart_front(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(cart__user_id=request.user)
    else:
        session_key = request.session.session_key
        if session_key:
            cart_items = CartItem.objects.filter(cart__session_key=session_key)
        else:
            cart_items = CartItem.objects.none()
    
    return render(request, 'cart.html', {'cart_items': cart_items})