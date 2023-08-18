from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import JuanViewSet,AzuilViewSet,AzuilViewSet,JuanViewSet,AzuilViewSet,JuanViewSet,AzuilViewSet,JuanViewSet

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register('juan', JuanViewSet )
router.register('azuil', AzuilViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
