from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, View, DetailView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Product, Cart, CartItem, Order, Category
from .forms import ProductForm, CustomUserCreationForm 


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
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
    

class ProductListView(ListView):
    paginate_by = 10
    model = Product
    template_name = 'store/product_list.html'
    context_object_name = 'products'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        category_id = self.request.GET.get('category')
        order_by = self.request.GET.get('order_by')
        queryset = Product.objects.all()
        
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )
        
        if category_id:
            queryset = queryset.filter(category_id=category_id)
            print('using category',category_id)
            
        if order_by:
            queryset = queryset.order_by(order_by)
            
        else:
            queryset = queryset.order_by('name')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    
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


class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product_detail.html'
    context_object_name = 'product'