import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Cash_machine.settings')

import django
django.setup()

from machine.models import Item
def create_items():
    items_list = Item.objects.bulk_create([
        Item(title="Choolate", price=135),
        Item(title="Icecream", price=150),
        Item(title="Сookie", price=25),
        Item(title="Сupcake", price=120),

    ])


create_items()
