from machine.models import Item
def ctreate_items():
    items_list = Item.objects.bulk_create([
        Item(title="Choolate", price=135),
        Item(title="Icecream", price=150),
        Item(title="Сookie", price=25),
        Item(title="Сupcake", price=120),

])