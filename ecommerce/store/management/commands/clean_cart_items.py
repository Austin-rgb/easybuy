
from django.core.management.base import BaseCommand
from store.models import CartItem
from django.db.models import Count

class Command(BaseCommand):
    help = 'Remove duplicate CartItem instances'

    def handle(self, *args, **kwargs):
        cart_items = CartItem.objects.values('cart_id', 'product_id').annotate(count=Count('id')).filter(count__gt=1)

        for item in cart_items:
            duplicates = CartItem.objects.filter(cart_id=item['cart_id'], product_id=item['product_id'])
            for duplicate in duplicates[1:]:
                duplicate.delete()

        self.stdout.write(self.style.SUCCESS('Successfully removed duplicate CartItems'))
