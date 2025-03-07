import os
import uuid
from datetime import datetime
import pdfkit
from django.http import HttpResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from jinja2 import Environment, FileSystemLoader
from machine.create_qr import generate_qr
from machine.models import Item
from machine.serializers import ItemsSerializer


def create_reciept(items):
    items_list = list(Item.objects.filter(id__in=items))
    env = Environment(loader=FileSystemLoader('media/sample_reciept'))
    template = env.get_template("receipt_temoplate.html")
    items = [{'name': item.title, 'total': item.price, 'quantity': 1} for item in items_list]
    total_price = sum(item['total'] for item in items)
    scratch_73 = template.render(
        {'date': datetime.now().strftime("%d.%m.%Y %H:%M"), 'items': items, 'total_cost': total_price})
    filename = f'media/{uuid.uuid4()}.pdf'
    config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
    pdfkit.from_string(scratch_73, f'{filename}', configuration=config, options={
        'page-height': "150",
        'page-width': "69"})
    generate_qr(filename)
    return filename


def send_file(request, filename):
    filename = filename
    file_directory = 'media/'  # Замените на путь к вашей директории с файлами
    file_path = os.path.join(file_directory, filename)
    # Проверка, существует ли файл
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            return response
    else:
        raise Http404("Файл не найден")


class CashMachineView(APIView):

    def post(self, request):
        serializer = ItemsSerializer(data=request.data)
        if serializer.is_valid():
            items = serializer.validated_data['items']
            create_reciept(items)
            image_data = open('media/QR-code/qr_code.png', 'rb').read()
            return HttpResponse(image_data, content_type='image/png')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
