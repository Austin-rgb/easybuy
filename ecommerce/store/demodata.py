
import string
import random

def random_date(month=0,day=1):
    year = 2024
    if month==0:
        month = random.randint(month,6)
    day = random.randint(day,29)
    return dict(year=year,month=month,day=day)

class Product:
    IMAGES = [
    'image1.png',
    'image2.png',
    'image3.png',
    'image4.png',
    'image5.png',
    'image6.png',
    'image7.png',
    'image8.png',
    'image9.png',
    'image0.png',
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
        return ' '.join(Product.name() for i in range(20))

    def image():
        return random.choice(Product.IMAGES)
    
    def delivery_info():
        return random.choice(Product.DELIVERY_OPTIONS)
    
    def remaining():
        return random.randint(0,1000)
    
    def price():
        return random.choice(Product.PRICE)
    

class Orders:
    STATES = [
        'preparing delivery',
        'delivery in progress',
        'delivered'
    ]
    
    def state():
        return random.choice(Orders.STATES)
    
    def product():
        return Product.name()
    
    def openned():
        return random_date()
    
    def deadline(month,day):
        return random_date(month,day)
    

def products(n=10)->list:
    products_ = []
    for i in range(n):
        product = {}
        product['name']=Product.name()
        product['description']=Product.description()
        product['image1']=Product.image()
        product['image2']=Product.image()
        product['image3']=Product.image()
        product['remaining']=Product.remaining()
        product['delivery']=Product.delivery_info()
        product['price']=Product.price()
        products_.append(product)
    return products_

def orders(n=10)->list:
    orders_ = []
    for i in range(n):
        order = {}
        order['state'] = Orders.state()
        order['product'] = Orders.product()
        order['openned on'] = Orders.openned()
        order['deadline'] = Orders.deadline(order['openned on']['month'],order['openned on']['day'])
        orders_.append(order)
    return orders_

