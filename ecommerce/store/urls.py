from django.urls import path, include 
from django.contrib.auth.views import LoginView
from .views import ProductListView, OrderListView, add_demo_data, add_to_cart, cart_detail, register
urlpatterns = [
    path('products/', ProductListView.as_view(),name='products'),
    path('orders/',OrderListView.as_view(),name='orders'),
    path('add_demo_data',add_demo_data, name='add_demo_data'), 
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_detail, name='cart_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
]
