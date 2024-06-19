from django.contrib import admin

from .models import Category, Order, Product, Cart, CartItem

admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
