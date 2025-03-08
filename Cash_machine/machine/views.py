import os
from django.http import HttpResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from machine.receipt import create_reciept
from machine.serializers import ItemsSerializer


class CashMachineView(APIView):

    def post(self, request):
        serializer = ItemsSerializer(data=request.data)
        if serializer.is_valid():
            items = serializer.validated_data['items']
            create_reciept(items)
            image_data = open('media/QR-code/qr_code.png', 'rb').read()
            return HttpResponse(image_data, content_type='image/png')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def send_file(request, filename):
    url_file = filename
    file_directory = 'media/'  # Замените на путь к вашей директории с файлами
    file_path = os.path.join(file_directory, url_file)
    # Проверка, существует ли файл
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{url_file}"'
            return response
    else:
        raise Http404("Файл не найден")
