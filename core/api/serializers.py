from rest_framework.serializers import ModelSerializer, IntegerField
from rest_framework.validators import UniqueValidator
from ..general.models import Category, BooksItems
from cart.api.models import CartItem


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductSerializer(ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = IntegerField(write_only=True)

    class Meta:
        model = BooksItems
        fields = '__all__'
        extra_kwargs = {
            'title': {
                'validators': [
                    UniqueValidator(
                        queryset=BooksItems.objects.all()
                    )
                ]
            },
        }

class AddToCartSerializer(ModelSerializer):
    quantity = IntegerField(min_value=1, required=True)

    class Meta:
        model = CartItem
        fields = ['quantity']