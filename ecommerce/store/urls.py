from django.urls import path
from .views import ProductListView, OrderListView, add_demo_data
urlpatterns = [
    path('products/', ProductListView.as_view(),name='products'),
    path('orders/',OrderListView.as_view(),name='orders'),
    path('add_demo_data',add_demo_data, name='add_demo_data')
]