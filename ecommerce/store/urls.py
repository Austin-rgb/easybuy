from django.urls import path, include 
from django.contrib.auth.views import LoginView
from .views import ProductListView, OrderListView, add_to_cart, cart_detail, register, upload_product, ProductDetailView
urlpatterns = [
    path('products/', ProductListView.as_view(),name='product_list'),
    path('orders/',OrderListView.as_view(),name='orders'), 
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_detail, name='cart_detail'),
    path('register/', register, name='register'),
    path('upload_product/', upload_product, name='upload_product'),
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('products/<int:pk>/',ProductDetailView.as_view(),name='product_detail'),
]
