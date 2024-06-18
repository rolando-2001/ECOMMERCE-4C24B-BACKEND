from rest_framework import serializers
from tienda.models import Furniture

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furniture
        fields = '__all__'