from rest_framework import serializers
from tienda.models import FurnitureCategory

class FurnitureCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FurnitureCategory
        fields = '__all__'