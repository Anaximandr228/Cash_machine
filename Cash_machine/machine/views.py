import os
import uuid
from datetime import datetime
import pdfkit
import qrcode as qrcode
from django.http import HttpResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from jinja2 import Environment, FileSystemLoader
from machine.models import Item
from machine.serializers import ItemsSerializer
from PIL import Image, ImageDraw


def createreciept(items):
    items_list = list(Item.objects.filter(id__in=items))
    env = Environment(loader=FileSystemLoader('media/sample_reciept'))
    template = env.get_template("scratch_73.html")
    items = [{'name': item.title, 'total': item.price, 'quantity': 1} for item in items_list]
    total_price = sum(item['total'] for item in items)
    scratch_73 = template.render(
        {'date': datetime.now().strftime("%d.%m.%Y %H:%M"), 'items': items, 'total_cost': total_price})
    filename = f'media/{uuid.uuid4()}.pdf'
    config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
    pdfkit.from_string(scratch_73, f'{filename}', configuration=config, options={
        'page-height': "150",
        'page-width': "69"})
    return filename

def send_file(request, filename):
        filename = filename
        file_directory = 'media/'  # Замените на путь к вашей директории с файлами
        file_path = os.path.join(file_directory, filename)
        img = qrcode.make(f'http://127.0.0.1:8000/media/{filename}')
        img.save("some_file.png")
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
            createreciept(items)
            return Response({"items": items}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
