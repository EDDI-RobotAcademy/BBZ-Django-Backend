from django.urls import path, include
from rest_framework.routers import DefaultRouter

from favorites.controller.views import FavoritesView

router = DefaultRouter()

router.register(r'favorites', FavoritesView, basename='favorites')

urlpatterns = [
    path('', include(router.urls)),
    path('register', FavoritesView.as_view({'post': 'favoritesRegister'}), name='favorites-register'),
    path('list', FavoritesView.as_view({'post': 'favoritesList'}), name='favorites-list'),
]