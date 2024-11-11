"""
URL configuration for bk_mall project.

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
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('cart/',views.show_cart,name='cart'),
    path('add_to_cart/',views.add_to_cart,name='add_to_cart'),
    path('',include('customers.urls')),
    path('remove_item/<pk>',views.remove_item,name='remove_item'),
    path('checkout',views.checkout,name='checkout'),
    path('orders',views.view_orders,name='orders'),


]
