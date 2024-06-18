from tienda.serializers import RevalidateTokenSerializer
from tienda.models import User
from tienda.serializers import UserSerializer


####################################################################################################
from rest_framework_simplejwt.views import TokenObtainPairView


####################################################################################################
from rest_framework import status
from rest_framework.authentication import get_authorization_header
from rest_framework.request import Request
from rest_framework.response import Response
import jwt


# Para iniciar sesion
class RevalidateToken(TokenObtainPairView):
    serializer_class = RevalidateTokenSerializer

    def get(self, request: Request, *args, **kwargs):
        auth_header = get_authorization_header(request).split()
        if not auth_header or auth_header[0].lower() != b"bearer":
            return Response(
                {"error": "Token no encontrado"}, status=status.HTTP_401_UNAUTHORIZED
            )

        token = auth_header[1].decode("utf-8")

        try:
            payload = jwt.decode(token, "SECRET_KEY", algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return Response(
                {"error": "Token expirado"}, status=status.HTTP_401_UNAUTHORIZED
            )

        user = User.objects.get(user_id=payload["user_id"])

        if not user:
            return Response(
                {"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND
            )
            
        user_serializer = UserSerializer(user)

        return Response(
            {
                "token": jwt.encode(
                    {"user_id": user.user_id},
                    "SECRET_KEY",
                    algorithm="HS256",
                ),
                "user": user_serializer.data,
            },
            status=status.HTTP_200_OK,
        )
