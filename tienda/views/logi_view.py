####################################################################################################
from tienda.serializers import UserSerializer, LoginSerializer


####################################################################################################
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

####################################################################################################
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
import jwt


# Para iniciar sesion
class Login(TokenObtainPairView):
    serializer_class = LoginSerializer

    # my_function(1, 2, 3, 4, 5, name='John', age=30)
    # def my_function(*args, **kwargs):

    def post(self, request: Request, *args, **kwargs):
        username = request.data.get("email")
        password = request.data.get("password")

        print(username)

        user = authenticate(username=username, password=password)

        if user:
            login_serializer = self.serializer_class(
                data={"username": username, "password": password}
            )

            if login_serializer.is_valid():
                user_serializer = UserSerializer(user)

                return Response(
                    {
                        "token": jwt.encode(
                            {"user_id": user_serializer.data["user_id"]},
                            "SECRET_KEY",
                            algorithm="HS256",
                        ),
                        "user": user_serializer.data,
                    },
                    status=status.HTTP_200_OK,
                )

            return Response(
                {"error": "Contraseña o usuario incorrecto"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {"error": "Contraseña o usuario incorrecto"},
            status=status.HTTP_400_BAD_REQUEST,
        )
