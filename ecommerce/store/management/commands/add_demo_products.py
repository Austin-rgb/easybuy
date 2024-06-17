# store/management/commands/add_demo_data.py

from django.core.management.base import BaseCommand
from store.models import Product
from .demodata import products
class Command(BaseCommand):
    help = 'Add demo data to the products table'

    def handle(self, *args, **kwargs):
        products_ = products('Laptops')
        for product_data in products_:
            Product.objects.create(**product_data)

        products_ = products('Smartphones')
        for product_data in products_:
            Product.objects.create(**product_data)

        products_ = products('Televisions')
        for product_data in products_:
            Product.objects.create(**product_data)

        products_ = products('Desktops')
        for product_data in products_:
            Product.objects.create(**product_data)

        self.stdout.write(self.style.SUCCESS('Successfully added demo data to the products table'))
