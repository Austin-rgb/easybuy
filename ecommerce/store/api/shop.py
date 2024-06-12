from booking import Booker
from peewee import Model

class Payment:
    def __init__(self) -> None:
        pass

    def confirm (account_no:str,payment_ref:str)->bool:
        return True

class Shelf:
    def __init__(self,items_model:Model,payment_api:Payment) -> None:
        self.items_model = items_model
        self.payment = payment_api

    def get_availables(self,**filters)->list:
        available_items = Booker. get_availables()
        items = []
        for available_item in available_items:
            filters['id'] = available_item
            items.append(self.items_model.select().where(filters))

        return items

    def get_item(self,item_id)->bool:
        item = self.items_model.select().where(id=item_id)
        return item

    def start_buying(self,item_id)->bool:
        pass

    def buy(item_id,payment_id)->bool:
        pass

    def add_item(self,**details)->str:
        item = self.items_model(details)
        item.save()

    def remove_item(self,item_id)->bool:
        item = self.items_model.get(id=item_id)
        item.delete()

    def get_statistics()->dict:
        pass

    def get_category_statistics(category)->dict:
        pass

    def get_item_statistics(item)->dict:
        pass