from django.urls import path
from .views import (PokemonList, PokemonDetail,
                    TypeList, TypeDetail) 
# from rest_framwork.routers import DefaultRouter

urlpatterns = [
    path('list/' ,PokemonList.as_view(),name='poke-list'),
    path('<int:pk>', PokemonDetail.as_view(),name='poke-detail'),
    path('type/list/' , TypeList.as_view(),name='type-list'),
    path('type/<int:pk>', TypeDetail.as_view(),name='type-detail'),
]
