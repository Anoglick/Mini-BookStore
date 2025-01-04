from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>', views.UserView.as_view())
]