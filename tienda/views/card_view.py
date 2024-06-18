from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tienda.models import Orders, Orderitems, Furniture
from django.utils import timezone

class CardViewSet(APIView):
    
    def post(self, request):
        data_card = request.data
        print(data_card)
        
        total_price = 0
        for item in data_card['cart']:
            print(f"ID: {item['id']}, Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}")
            total_price += float(item['price']) * item['quantity']

            try:
                furniture = Furniture.objects.get(furniture_id=item['id'])  # Cambiado de furniture_id a id
            except Furniture.DoesNotExist:
                return Response({"error": f"Furniture with id {item['id']} does not exist"}, status=status.HTTP_404_NOT_FOUND)
            
            # Guardar cada ítem del carrito en la base de datos
            order_item = Orderitems.objects.create(
                order=None,  # Aún no tenemos el ID de la orden
                product=furniture,
                quantity=item['quantity'],
                price=item['price']
            )

        print(f"Total price: {total_price}")  

        user_id = data_card['user']
        print(f"User ID: {user_id}")  # Acceder al campo 'user'

        # Crear la orden en la base de datos
        order = Orders.objects.create(
            user_id=user_id,
            total_price=total_price,
            created_at=timezone.now(),
            updated_at=timezone.now(),
        )

        # Actualizar el order_id en cada Orderitem con el ID de la orden creada
        Orderitems.objects.filter(order=None).update(order=order)

        return Response({"message": 'Se agregó al carrito y se creó la orden'}, status=status.HTTP_200_OK)
