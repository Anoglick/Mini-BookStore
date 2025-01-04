from django.urls import path
from . import views

urlpatterns = [
    path(f'', views.Categories.as_view(), name='api-categories'),
    path(f'<int:pk>', views.OneCategory.as_view(), name='api-categories-detail'),
    path(f'items', views.APIProductItem.as_view(), name='api-items'),
    path(f'<int:category_id>/items', views.APIProductItem.as_view(), name='api-category-items'),
    path('<int:category_id>/items/<int:pk>', views.ProductItemByID.as_view(), name='items-detail'),
    path('add-to-cart/<int:product_id>', views.AddToCartAPIView.as_view(), name='add_to_cart')
]