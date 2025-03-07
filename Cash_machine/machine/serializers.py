from rest_framework import serializers


class ItemsSerializer(serializers.Serializer):
    items = serializers.ListField(
        child=serializers.IntegerField(),
        allow_empty=False
    )
