"""
URL configuration for settings project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('other_pages.urls')),
    path('categories/', include('core.frontend.urls')),
    path('api/categories/', include('core.api.urls')),
    path('api/user/', include('users.api.urls')),
    path('user/', include('users.frontend.urls')),
    path('cart/', include('cart.frontend.urls')),
    path('api/cart/', include('cart.api.urls')),

    path('auth/', include('auth.urls')),
]
