from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Importar todas las vistas necesarias
from tienda.views import (
    Login,
    UserViewSet,
    FurnitureViewSet,
    FurnitureCategoryViewSet
)

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('furniture', FurnitureViewSet)
router.register('furniture-categories', FurnitureCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', Login.as_view(), name='login'),
]
