from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    category = models.CharField(max_length=32)
    name = models.CharField(max_length=200)
    description = models.TextField()
    image1 = models.CharField(max_length=64)
    image2 = models.CharField(max_length=64)
    image3 = models.CharField(max_length=64)
    delivery = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    available = models.BooleanField()

    def __str__(self):
        return self.name
    


class Order(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    openned = models.DateTimeField()
    status = models.CharField(max_length=64)