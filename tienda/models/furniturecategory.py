from django.db import models

class FurnitureCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    


    def __str__(self):
        return self.name