from django.contrib import admin
from .models import FurnitureCategory, Furniture,Orders,Orderitems

# Register your models here.

class FurnitureCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    ordering = ['name']  # Ordena por nombre de categoría
    list_per_page = 20  # Número de registros por página

class FurnitureAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock']
    search_fields = ['name']
    ordering = ['name']  # Ordena por nombre de mueble
    list_per_page = 20  # Número de registros por página

class OrdersAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'user', 'total_price', 'created_at']
    search_fields = ['order_id']
    ordering = ['order_id']  # Ordena por id de orden
    list_per_page = 20  # Número de registros por página

class OrderitemsAdmin(admin.ModelAdmin):
    list_display = ['order_item_id', 'product', 'quantity', 'price']
    search_fields = ['order_item_id']
    ordering = ['order_item_id']  # Ordena por id de item de orden
    list_per_page = 20  # Número de registros por página

admin.site.register(Orderitems, OrderitemsAdmin)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(FurnitureCategory, FurnitureCategoryAdmin)
admin.site.register(Furniture, FurnitureAdmin)
