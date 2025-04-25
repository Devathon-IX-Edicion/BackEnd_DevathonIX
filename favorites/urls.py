from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FavoriteRecipeViewSet

router = DefaultRouter()
router.register(r'favorites', FavoriteRecipeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('v1/favorites/', FavoriteRecipeViewSet.as_view({'get': 'list'}), name='favorite-recipes-list'),   
]