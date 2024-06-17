
import string
import random
from ...models import Product, Order
def random_date(month=0,day=1):
    year = 2024
    if month==0:
        month = random.randint(month,6)
    day = random.randint(day,29)
    return dict(year=year,month=month,day=day)

class Products:
    IMAGES = [
    'image1.jpeg',
    'image2.jpeg',
    'image3.jpeg',
    'image4.jpeg',
    'image5.jpeg',
    'image6.jpeg',
    'image7.jpeg',
    'image8.jpeg',
    'image9.jpeg',
    'image0.jpeg',
    ]

    DELIVERY_OPTIONS = [
        'free country wide',
        'free within cbd',
        'ksh. 100',
        'ksh. 200'
    ]

    PRICE = [
        1000,
        2000,
        3000,
        4000,
        5000
    ]
    def name(wordlength=5):
        vowels = ''.join(random.choices('aeiou',k=wordlength))
        consonunts = ''.join(random.choices(string.ascii_lowercase,k=wordlength))
        return ''.join([a+b for a,b in zip(consonunts,vowels)])
    
    def description():
        return ' '.join(Products.name() for i in range(20))

    def image(category):
        return f'product_images/{category}{random.randint(1,10)}.jpeg'
    
    def delivery_info():
        return random.choice(Products.DELIVERY_OPTIONS)
    
    def remaining():
        return random.randint(0,1000)
    
    def price():
        return random.choice(Products.PRICE)
    

class Orders:
    STATES = [
        'preparing delivery',
        'delivery in progress',
        'delivered'
    ]
    
    def state():
        return random.choice(Orders.STATES)
    
    def product():
        return Products.name()
    
    def openned():
        return random_date()
    
    def deadline(month,day):
        return random_date(month,day)
    
categories= {
    'Laptops':1,
    'Smartphones':2,
    'Desktops':3,
    'Televisions':4,
}

def products(category, n=20)->list:
    products_ = []
    for i in range(n):
        product = dict(
            category_id = categories[category],
            name=Products.name(),
            description=Products.description(),
            image=Products.image(category),
            image1=Products.image(category ),
            image2=Products.image(category ),
            image3=Products.image(category ),
            stock=Products.remaining(),
            delivery=Products.delivery_info(),
            price=Products.price(),
            available = True,
            )
        products_.append(product)

    return products_
        

def orders(n=10)->list:
    for i in range(n):
        order = Order(
            state = Orders.state(),
            product= Orders.product(),
            openned = Orders.openned(),
            deadline = Orders.deadline()
        )
        order.save()

