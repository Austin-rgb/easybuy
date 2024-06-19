from .models import Order, Product
import random
import string
class Payment:
    def __init__(self) -> None:
        self.payments = {}

    def pay(self, amount:float)->str:
        ref_code = ''.join(random.choices(string.ascii_uppercase,k=10))
        self.payments[ref_code]=amount
        return ref_code

    def confirm (self,ref_code:str)->float:
        amount = self.payments.get(ref_code)
        print('confirming:',ref_code)
        print('amount:',amount)
        return amount


class Shelf:
    def __init__(self, payment=Payment()) -> None:
        self.payment = payment    
    
    def buy(self,item_id,payment_id, quantity, user_id)->bool:
        product = Product.objects.get(id=item_id)
        bill = product.price * quantity
        if self.payment.confirm(payment_id)==bill:
            product.stock -= quantity
            order = Order(
                product = item_id,
                quantity = quantity,
                user = user_id
            )
            order.save()
            product.save()
            return True
        return False

    def update_stock(self,item_id, quantity):
        product = Product.objects.get(id=item_id)
        product.stock += quantity