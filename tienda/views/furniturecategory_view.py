from rest_framework import viewsets
from tienda.models import FurnitureCategory
from tienda.serializers import FurnitureCategorySerializer
from rest_framework.permissions import AllowAny


class FurnitureCategoryViewSet(viewsets.ModelViewSet):
    queryset = FurnitureCategory.objects.all()
    serializer_class = FurnitureCategorySerializer
    permission_classes = [AllowAny]  # Permite acceso sin autenticación JWT