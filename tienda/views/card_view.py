from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from tienda.models import Orders, Orderitems, Furniture
from rest_framework.authentication import get_authorization_header
from django.utils import timezone
import jwt
from tienda.serializers import CardSerializer

class CardViewSet(TokenObtainPairView):
    serializer_class = CardSerializer
    
    def post(self, request):
        auth_header = get_authorization_header(request).split()
        if not auth_header or auth_header[0].lower() != b"bearer":
            return Response(
                {"error": "Token no encontrado"}, status=status.HTTP_401_UNAUTHORIZED
            )

        token = auth_header[1].decode("utf-8")
        user_id = jwt.decode(token, "SECRET_KEY", algorithms=["HS256"])["user_id"]

        data_card = request.data

        total_price = 0
        for item in data_card['cart']:
            total_price += float(item['price']) * item['quantity']

            try:
                furniture = Furniture.objects.get(furniture_id=item['id'])  # Cambiado de furniture_id a id
            except Furniture.DoesNotExist:
                return Response({"error": f"Furniture with id {item['id']} does not exist"}, status=status.HTTP_404_NOT_FOUND)

            # Guardar cada ítem del carrito en la base de datos
            Orderitems.objects.create(
                order=None,  # Aún no tenemos el ID de la orden
                product=furniture,
                quantity=item['quantity'],
                price=item['price']
            )

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
