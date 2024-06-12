from django.db.models import Model, CharField, IntegerField
from django.contrib.auth.models import User


class Available(Model):
    item_key = CharField (max_length=32)
    quantity = IntegerField()



class Booking(Model):
    item_key = CharField(max_length=32)
    user_id = CharField (max_length=32)
    quantity = IntegerField()

