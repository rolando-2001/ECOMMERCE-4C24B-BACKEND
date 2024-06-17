from django.contrib import admin
from .models import FurnitureCategory, Furniture,Pay

# Register your models here.
admin.site.register(FurnitureCategory)
admin.site.register(Furniture)
admin.site.register(Pay)