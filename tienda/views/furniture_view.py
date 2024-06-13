from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from tienda.models import Furniture
from tienda.serializers import FurnitureSerializer

class FurnitureViewSet(viewsets.ModelViewSet):
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer
    permission_classes = [AllowAny]  # Permite acceso sin autenticación JWT
