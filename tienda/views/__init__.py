from .logi_view import Login
from .revalidate_token_view import RevalidateToken
from .furniture_view import FurnitureViewSet
from .user_view import UserViewSet
from .furniturecategory_view import FurnitureCategoryViewSet
from .furniturerelated_view import FurnitureByCategoryViewSet
from .register_view import Register
from .pay_view import PayViewSet
from .card_view import CardViewSet


from .orders_view import UserOrderListView

__all__=[

    'Login',
    'Register'
    'RevalidateToken',
    'FurnitureViewSet',
    'UserViewSet',

    'FurnitureCategoryViewSet',
    'FurnitureByCategoryViewSet',

    'Register',
    'PayViewSet'

    # 'CardViewSet'
    , 'CardViewSet',

    'UserOrderListView'
  
    
]