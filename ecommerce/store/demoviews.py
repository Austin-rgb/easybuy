from demodata import products,orders

def available_products():
    products = products()
    context = {}
    context['products'] = products
    # return render_template('available_products.html', context = context)
    
def orders():
    orders  = orders()
    context = {}
    context['orders'] = orders
    # return render_template('orders.html', context = context)