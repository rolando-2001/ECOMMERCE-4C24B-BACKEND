from rest_framework import serializers
from tienda.models import Furniture

class FurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furniture
        fields = '__all__'