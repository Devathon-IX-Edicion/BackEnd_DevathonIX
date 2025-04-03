from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EffectViewSet

router = DefaultRouter()
router.register(r'effects', EffectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]