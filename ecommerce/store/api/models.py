
from peewee import CharField, IntegerField, Model, SqliteDatabase

db = SqliteDatabase('my_database.db')

class Available(Model):
    item_key = CharField (max_length=32)
    quantity = IntegerField()

    class Meta:
        database =db


class Booking(Model):
    item_key = CharField(max_length=32)
    user_id = CharField (max_length=32)
    quantity = IntegerField()

    class Meta:
        database =db


with db:
    db.create_tables([Available,Booking])