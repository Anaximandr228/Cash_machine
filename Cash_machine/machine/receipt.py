import uuid
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
import pdfkit

from Cash_machine.settings import WKHTMLTOPDF_PATH
from machine.models import Item

from machine.create_qr import generate_qr


# Функция создания чека
def create_reciept(items):
    env = Environment(loader=FileSystemLoader('media/sample_reciept'))
    template = env.get_template("receipt_template.html")
    items_list = list(Item.objects.filter(id__in=items))
    items_dict = {}
    for item_id in items:
        item = next((i for i in items_list if i.id == item_id), None)
        if item:
            if item.id in items_dict:
                items_dict[item.id]['quantity'] += 1  # Увеличиваем количество
            else:
                # Если элемента нет, добавляем его в словарь
                items_dict[item.id] = {
                    'name': item.title,
                    'total': item.price,
                    'quantity': 1
                }
    items = list(items_dict.values())
    total_price = sum(item['total'] * item['quantity'] for item in items)
    sample_reciept = template.render(
        {'date': datetime.now().strftime("%d.%m.%Y %H:%M"), 'items': items, 'total_cost': total_price})
    filename = f'media/{uuid.uuid4()}.pdf'
    config = pdfkit.configuration(wkhtmltopdf=f"{WKHTMLTOPDF_PATH}")
    pdfkit.from_string(sample_reciept, f'{filename}', configuration=config, options={
        'page-height': "150",
        'page-width': "69"})
    generate_qr(filename)
    return filename
