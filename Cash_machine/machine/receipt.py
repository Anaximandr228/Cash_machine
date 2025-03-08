import uuid
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
import pdfkit
from machine.models import Item
from machine.create_qr import generate_qr


def create_reciept(items):
    items_list = list(Item.objects.filter(id__in=items))
    env = Environment(loader=FileSystemLoader('media/sample_reciept'))
    template = env.get_template("receipt_template.html")
    items = [{'name': item.title, 'total': item.price, 'quantity': 1} for item in items_list]
    total_price = sum(item['total'] for item in items)
    sample_reciept = template.render(
        {'date': datetime.now().strftime("%d.%m.%Y %H:%M"), 'items': items, 'total_cost': total_price})
    filename = f'media/{uuid.uuid4()}.pdf'
    config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
    pdfkit.from_string(sample_reciept, f'{filename}', configuration=config, options={
        'page-height': "150",
        'page-width': "69"})
    generate_qr(filename)
    return filename

