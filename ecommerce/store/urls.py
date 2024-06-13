from django.urls import path
from django.contrib.auth.views import LoginView
from .views import ProductListView, OrderListView, add_demo_data, add_to_cart, cart_detail
urlpatterns = [
    path('products/', ProductListView.as_view(),name='products'),
    path('orders/',OrderListView.as_view(),name='orders'),
    path('add_demo_data',add_demo_data, name='add_demo_data'), 
    path('login',LoginView.as_view(),name='login'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_detail, name='cart_detail'),
]
