from django.shortcuts import render, HttpResponse

# Create your views here.
from django.views.generic import ListView, View

from .models import Product, Order

from .demodata import products

def add_demo_data(request):
    products()
    return HttpResponse('done')

class ProductListView(ListView):
    paginate_by = 10
    model = Product
    template_name = 'store/product_list.html'
    context_object_name = 'products'
    queryset = Product.objects.filter(available=True)
    

class OrderListView(ListView):
    paginate_by = 10
    model = Order

class PaymentView(View):
    def get():
        products()

    def post():
        pass

class AddItemView(View):
    def get():
        pass

    def post():
        pass

class ProductView(View):
    pass