from tienda.views.logi_view import Login
from tienda.views.furniture_view import FurnitureViewSet
from tienda.views.user_view import UserViewSet
from tienda.views.furniturecategory_view import FurnitureCategoryViewSet
from tienda.views.furniturerelated_view import FurnitureByCategoryViewSet


__all__=[
    'Login',
    'FurnitureViewSet',
    'UserViewSet',
    'FurnitureCategoryViewSet',
    'FurnitureByCategoryViewSet'

]