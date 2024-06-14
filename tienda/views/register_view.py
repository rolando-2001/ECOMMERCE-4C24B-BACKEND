from tienda.serializers import  RegisterSerializer
from tienda.models import User


####################################################################################################
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

####################################################################################################
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView


# Para iniciar sesion
class Register(TokenObtainPairView):
    serializer_class = RegisterSerializer

    # my_function(1, 2, 3, 4, 5, name='John', age=30)
    # def my_function(*args, **kwargs):

    def post(self, request: Request, *args, **kwargs):
        name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        email = request.data.get("email")
        password = request.data.get("password")
        
        if not name or not last_name or not email or not password:
            return Response(
                {"error": "Todos los campos son requeridos"}, status=status.HTTP_400_BAD_REQUEST
            )

        if User.objects.filter(email=email).exists():
            return Response(
                {"error": "El email ya esta en uso"}, status=status.HTTP_400_BAD_REQUEST
            )

        if len(password) < 8:
            return Response(
                {"error": "La contraseña debe tener al menos 8 caracteres"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        User.objects.create_user(
            first_name=name, last_name=last_name, email=email, password=password, username=email
        )

        return Response(
            {"message": "Usuario creado exitosamente"}, status=status.HTTP_201_CREATED
        )
