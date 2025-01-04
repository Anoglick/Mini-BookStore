from django.db.models import (Model, CharField, TextField, 
                            ForeignKey, SlugField,
                            IntegerField, CASCADE,
                            DateField, ImageField,
                            DateTimeField, PositiveIntegerField)

from django.contrib.auth.models import User
from core.general.models import BooksItems

class Cart(Model):
    user_id = ForeignKey(User, on_delete=CASCADE, null=True, blank=True)
    session_key = CharField(max_length=50, null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)

class CartItem(Model):
    product_id = ForeignKey(BooksItems, on_delete=CASCADE)
    quantity = PositiveIntegerField(default=1)
    price = IntegerField()
    cart = ForeignKey(Cart, related_name='items', on_delete=CASCADE)

    class Meta:
        unique_together = ('cart', 'product_id')