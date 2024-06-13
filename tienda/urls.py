from django.urls import path,include
from rest_framework.routers import DefaultRouter

###################################################

from tienda.views import Login
from tienda.views import UserViewSet
###################################################


router = DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', include(router.urls) ,name="register"),

    path('login/', Login.as_view(), name='login')


]