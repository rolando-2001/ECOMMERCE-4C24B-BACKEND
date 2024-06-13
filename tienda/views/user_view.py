from rest_framework import viewsets
from tienda.models import User
from  tienda.serializers  import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer