from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, View
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .demodata import products
from .models import Product, Cart, CartItem, Order
from .forms import ProductForm, CustomUserCreationForm 


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'store/register.html', {'form': form})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    total = sum(item.product.price * item.quantity for item in cart.items.all())
    return render(request, 'store/cart_detail.html', {'cart': cart, 'total': total})
    

def add_demo_data(request):
    products()
    return HttpResponse('done')

class ProductListView(ListView):
    paginate_by = 10
    model = Product
    template_name = 'store/product_list.html'
    context_object_name = 'products'
    queryset = Product.objects.filter(available=True)
    
def upload_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'store/upload_product.html', {'form': form})

class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'store/order_list.html'
    context_object_name = 'orders'
    paginate_by = 10  # Adjust as needed

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-openned')


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
