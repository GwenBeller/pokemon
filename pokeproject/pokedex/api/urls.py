from django.urls import path
from .views import PokemonList, PokemonDetail 
# from rest_framwork.routers import DefaultRouter

urlpatterns = [
    path('list/' ,PokemonList.as_view(),name='poke-list'),
    path('<int:pk>', PokemonDetail.as_view(),name='poke-detail'),
    path('list/<int:pk>', PokemonDetail.as_view(),name='poke-detail'),
]
