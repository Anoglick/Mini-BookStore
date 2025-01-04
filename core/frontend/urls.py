from django.urls import path
from . import views

urlpatterns = [
    path('', views.categories_page, name='categories'),
    path('add', views.add_category, name='add-category'),
    path('items', views.items_page, name='items'),
    path('<int:category_id>/items', views.items_page, name='category-items'),
    path('<int:category_id>/items/<int:pk>', views.item_page, name='book-detail'),
    path('<int:category_id>/items/add', views.add_item, name='add-item'),
    path('<int:category_id>/items/<int:pk>/edit', views.edit_item, name='edit-item'),
    path('<int:category_id>/edit', views.edit_category, name='edit-category'),
    path('add-to-cart/<int:product_id>', views.add_to_cart, name='add-to-cart'),
]