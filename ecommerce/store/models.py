from django.db import models
from django.contrib.auth.models import User
from .storage import NonLockingFileSystemStorage

non_locking_storage = NonLockingFileSystemStorage()

class Category (models.Model):
    name = models.CharField(max_length=16)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default='general')
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/', null=True, blank=True, storage=non_locking_storage)
    image1 = models.ImageField(upload_to='product_images/', null=True, blank=True,storage=non_locking_storage)
    image2 = models.ImageField(upload_to='product_images/', null=True, blank=True,storage=non_locking_storage)
    image3 = models.ImageField(upload_to='product_images/', null=True, blank=True,storage=non_locking_storage)
    delivery = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    available= models.BooleanField()

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

from datetime import datetime

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    reference_code = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='cart_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('cart', 'product')
