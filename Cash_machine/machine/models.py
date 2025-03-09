from django.db import models

# Модель Item
class Item(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField(null=True)
