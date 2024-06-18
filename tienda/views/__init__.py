from tienda.views.logi_view import Login
from tienda.views.furniture_view import FurnitureViewSet
from tienda.views.user_view import UserViewSet
from tienda.views.furniturecategory_view import FurnitureCategoryViewSet
from tienda.views.furniturerelated_view import FurnitureByCategoryViewSet
from tienda.views.register_view import Register
from tienda.views.revalidate_token_view import RevalidateToken



__all__=[
    'Login',
    'Register',
    'RevalidateToken',
    'FurnitureViewSet',
    'UserViewSet',
    'FurnitureCategoryViewSet',
    'FurnitureByCategoryViewSet'
    

]