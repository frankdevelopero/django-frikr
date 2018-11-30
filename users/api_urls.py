from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.api import UserViewSet


# APIRouter
router = DefaultRouter()
router.register('users', UserViewSet, base_name='user')


urlpatterns = [

    # API URLs
    path(r'1.0/', include(router.urls)),  # Incluye las URLs de API

]
