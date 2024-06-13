from django.db import models
from .furniturecategory import FurnitureCategory

class Furniture(models.Model):
    furniture_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.CharField(max_length=500)
    category = models.ForeignKey(FurnitureCategory, on_delete=models.CASCADE)

