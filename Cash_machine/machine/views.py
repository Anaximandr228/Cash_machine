from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from machine.serializers import ItemsSerializer


class CashMachineView(APIView):

    def post(self, request):
        serializer = ItemsSerializer(data=request.data)
        if serializer.is_valid():
            items = serializer.validated_data['items']
            return Response({"items": items}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
