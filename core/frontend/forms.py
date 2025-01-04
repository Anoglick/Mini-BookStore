from django.forms import ModelForm, IntegerField
from ..general.models import Category, BooksItems

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class BookForm(ModelForm):
    class Meta:
        model = BooksItems
        fields = '__all__'
