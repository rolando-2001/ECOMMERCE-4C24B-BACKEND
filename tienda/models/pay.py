from django.db import models
from tienda.models import (User,Furniture)

class Pay(models.Model):
    pay_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    furniture = models.ForeignKey(Furniture, on_delete=models.CASCADE)
    pay_date = models.DateTimeField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    pay_method = models.CharField(max_length=250)
    
   
    
    class Meta:
        db_table = 'pay'
       