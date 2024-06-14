from tienda.views.logi_view import Login
from tienda.views.furniture_view import FurnitureViewSet
from tienda.views.user_view import UserViewSet
from tienda.views.furniturecategory_view import FurnitureCategoryViewSet
from tienda.views.furniturerelated_view import FurnitureByCategoryViewSet
from tienda.views.register_view import Register


__all__=[
    'Login',
    'Register'
    'FurnitureViewSet',
    'UserViewSet',
    'FurnitureCategoryViewSet',
    'FurnitureByCategoryViewSet'
    

]