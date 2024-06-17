from django.db import models
from .order import Orders
from .furniture import Furniture

class Orderitems(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    order= models.ForeignKey(Orders, on_delete=models.CASCADE , null=True)
    product= models.ForeignKey(Furniture, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


