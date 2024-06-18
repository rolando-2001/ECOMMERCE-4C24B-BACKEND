# serializers.py
from rest_framework import serializers
from tienda.models import Orders,User, Furniture, Orderitems



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class FurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furniture
        fields = ['name', 'price', 'image']

class OrderitemsSerializer(serializers.ModelSerializer):
    product = FurnitureSerializer()
    class Meta:
        model = Orderitems
        fields = ['quantity', 'product']

class OrdersSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    order_items = OrderitemsSerializer(many=True)

    class Meta:
        model = Orders
        fields = ['total_price', 'user', 'order_items']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['order_items'] = [
            {
                'name': item.product.name,
                'price': item.product.price,
                'quantity': item.quantity,
                'image': item.product.image
            } for item in instance.order_items.all()
        ]
        return representation