from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Importar todas las vistas necesarias
from tienda.views import (
    Register,
    Login,
    UserViewSet,
    FurnitureViewSet,
    FurnitureCategoryViewSet,
    FurnitureByCategoryViewSet
)

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('furniture', FurnitureViewSet)
router.register('furniture-categories', FurnitureCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login', Login.as_view(), name='login'),
    path('auth/register', Register.as_view(), name='register'),
    path('furniture-category/<int:category_id>/', FurnitureByCategoryViewSet.as_view({'get': 'retrieve'}), name='furniture-category'),
]