from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Importar todas las vistas necesarias
from tienda.views import (
    Register,
    Login,
    RevalidateToken,
    UserViewSet,
    FurnitureViewSet,

    FurnitureCategoryViewSet,
    FurnitureByCategoryViewSet,

    PayViewSet,

   # CardViewSet
   CardViewSet,

   # UserOrdersView
    UserOrderListView

)

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('furniture', FurnitureViewSet)
router.register('furniture-categories', FurnitureCategoryViewSet)

router.register('pay', PayViewSet)



urlpatterns = [
    path('', include(router.urls)),

    path('auth/login', Login.as_view(), name='login'),

    path('auth/register', Register.as_view(), name='register'),
    path('auth/revalidate-token', RevalidateToken.as_view(), name='revalidate-token'),
    path('payment/create', CardViewSet.as_view(), name='card'),

    #oreder list
    path('user-orders/<int:user_id>/', UserOrderListView.as_view(), name='user-order-list'),

    path('furniture-category/<int:category_id>/', FurnitureByCategoryViewSet.as_view({'get': 'retrieve'}), name='furniture-category'),
]