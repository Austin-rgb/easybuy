from .demodata import products,orders
from django.http import HttpResponse
from json import dumps

def available_products(request):
    products_ = products()
    context = {}
    context['products'] = products_
    # return render_template('available_products.html', context = context)
    return HttpResponse(dumps(products_))
    
def orders(request):
    orders_  = orders()
    context = {}
    context['orders'] = orders_
    # return render_template('orders.html', context = context)
    return HttpResponse(dumps(orders_))