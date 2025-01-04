from django.urls import path
from . import views

urlpatterns = [
    path('', views.CartRead.as_view()),
    path('update/<int:product_id>', views.CartUpdate.as_view(), name='cart-update'),
]