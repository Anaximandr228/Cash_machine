from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from machine.models import Item


# class ItemsSerializer(ModelSerializer):
#     class Meta:
#         model = Item
#         fields = ['id', 'title', 'price']

class ItemsSerializer(serializers.Serializer):
    items = serializers.ListField(
        child=serializers.IntegerField(),
        allow_empty=False
    )