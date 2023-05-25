from django.urls import path

from . import views

urlpatterns = [
    path('', views.PokemonSearchView.as_view(), name='pokemon_search'),
    path('pokemon_detail/', views.pokemon_detail, name='pokemon_detail'),
    path('favorite-pokemon/', views.PokemonCreateView.as_view(), name='favorite-pokemon'),
    path('favorite-pokemon/my-pokemon/', views.pokemon_list, name='pokemon_list'),
    path('favorite-pokemon/my-pokemon/<int:pk>', views.single_pokemon_detail, name='single_pokemon_detail')

]
