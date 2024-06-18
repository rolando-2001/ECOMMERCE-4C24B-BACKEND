# views.py
# views.py

from django.db import connection
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.authentication import get_authorization_header
from tienda.serializers import OrdersSerializer
import jwt
from rest_framework import status

class UserOrderListView(TokenObtainPairView):
    serializer_class = OrdersSerializer
    
    def get(self, request):
        auth_header = get_authorization_header(request).split()
        if not auth_header or auth_header[0].lower() != b"bearer":
            return Response(
                {"error": "Token no encontrado"}, status=status.HTTP_401_UNAUTHORIZED
            )

        token = auth_header[1].decode("utf-8")
        user_id = jwt.decode(token, "SECRET_KEY", algorithms=["HS256"])["user_id"]
        
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT tienda_user.username, tienda_user.first_name, tienda_furniture.name, tienda_furniture.price, 
                       orders.total_price, tienda_orderitems.quantity, tienda_furniture.image
                FROM orders
                JOIN tienda_orderitems ON tienda_orderitems.order_id = orders.order_id
                JOIN tienda_furniture ON tienda_orderitems.product_id = tienda_furniture.furniture_id
                JOIN tienda_user ON orders.user_id = tienda_user.user_id
                WHERE orders.user_id = %s
            """, [user_id])
            rows = cursor.fetchall()

        # Construir la respuesta JSON
        result = []
        for row in rows:
            result.append({
                'username': row[0],
                'first_name': row[1],
                'product_name': row[2],
                'product_price': row[3],
                'total_price': row[4],
                'quantity': row[5],
                'product_image': row[6],
            })

        return Response(result)
