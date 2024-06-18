from rest_framework import viewsets
from tienda.models import Pay
from tienda.serializers import PaySerializer

class PayViewSet(viewsets.ModelViewSet):
    queryset = Pay.objects.all()
    serializer_class = PaySerializer