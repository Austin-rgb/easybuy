# store/management/commands/add_demo_data.py

from django.core.management.base import BaseCommand
from store.models import Product

class Command(BaseCommand):
    help = 'Add demo data to the products table'

    def handle(self, *args, **kwargs):
        products = [
            {
                'name': 'Product 6',
                'description': 'Description for product 6',
                'price': 10.00,
                'stock':20,
                'available':True,
                'image': 'product_images/image6.jpeg'
            },
            {
                'name': 'Product 5',
                'description': 'Description for product 5',
                'price': 15.00,
                'stock':20,
                'available':True,
                'image': 'product_images/image5.jpeg'
            },
            {
                'name': 'Product 4',
                'description': 'Description for product 4',
                'price': 20.00,
                'stock':20,
                'available':True,
                'image': 'product_images/image4.jpeg'
            },
            {
                'name': 'Product 7',
                'description': 'Description for product 7',
                'price': 10.00,
                'stock':20,
                'available':True,
                'image': 'product_images/image5.jpeg'
            },
            {
                'name': 'Product 8',
                'description': 'Description for product 8',
                'price': 15.00,
                'stock':20,
                'available':True,
                'image': 'product_images/image8.jpeg'
            },
            {
                'name': 'Product 9',
                'description': 'Description for product 9',
                'price': 20.00,
                'stock':20,
                'available':True,
                'image': 'product_images/image9.jpeg'
            },
            # Add more products as needed
        ]

        for product_data in products:
            Product.objects.create(**product_data)

        self.stdout.write(self.style.SUCCESS('Successfully added demo data to the products table'))
