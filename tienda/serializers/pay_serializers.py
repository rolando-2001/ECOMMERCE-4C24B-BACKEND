from rest_framework import serializers
from tienda.models import Pay


class PaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pay
        fields = [ 'user', 'furniture', 'pay_date', 'total', 'pay_method']
