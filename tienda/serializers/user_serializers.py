from rest_framework import serializers
from tienda.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class LoginSerializer(TokenObtainPairSerializer):
    pass


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
                  'user_id', 
                  'first_name', 
                  'last_name', 
                  'email', 
                  'password'
                 ]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
                  'user_id', 
                  'first_name', 
                  'last_name', 
                  'email', 
                  'password'
                 ]