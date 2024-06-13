from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from tienda.models import Furniture, FurnitureCategory
from tienda.serializers import FurnitureSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny

class FurnitureByCategoryViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny] 
    def retrieve(self, request, category_id):
        try:
            category = FurnitureCategory.objects.get(category_id=category_id)
        except FurnitureCategory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        furniture = Furniture.objects.filter(category=category)
        serializer = FurnitureSerializer(furniture, many=True)
        return Response(serializer.data)