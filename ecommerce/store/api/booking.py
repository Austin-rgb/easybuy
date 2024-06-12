from models import Available, Booking

class Booker:
    def add_item(item_key:str,quantity:int):
        available = Available(item_key=item_key,quantity=quantity)
        available.save ()

    def book_item(item_key:str,user_id:str,quantity:int):
        item = Available.get_or_none(item_key=item_key)

        if item.quantity>=quantity:
            booking = Booking(item_key=item_key, user_id=user_id,quantity=quantity)
            item.quantity -= quantity
            if item.quantity==0:
                item.delete_instance()

            else:
                item.save()

            booking.save()
            return True
        else:
            return False

    def get_availables():
        availables = Available.select()
        return [available.item_key for available in availables]

    def is_booked(item_key):
        item = Available.get_or_none(item_key)
        if item:
            return True
        else:
            return False

    def get_user_bookings(user_id:str):
        bookings = Booking.select().where(user_id=user_id)
        return [booking.item_key for booking in bookings]