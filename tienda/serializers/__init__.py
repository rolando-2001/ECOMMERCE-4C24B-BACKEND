from tienda.serializers.user_serializers import UserSerializer,LoginSerializer, RegisterSerializer, RevalidateTokenSerializer
from tienda.serializers.furniture_serializers import FurnitureSerializer
from  tienda.serializers.furniturecategory_serializers import FurnitureCategorySerializer

__all__=[
    'UserSerializer',
    'LoginSerializer',
    'RegisterSerializer',
    'RevalidateTokenSerializer'
    'FurnitureSerializer',
    'FurnitureCategorySerializer'
    
]