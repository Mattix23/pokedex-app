from django.urls import path

from . import views

urlpatterns = [
    path('search-pokemon', views.PokemonSearchView.as_view(), name='pokemon_search'),
    path('pokemon_detail/', views.pokemon_detail, name='pokemon_detail'),
    path('favorite-pokemon/new', views.PokemonCreateView.as_view(), name='favorite-pokemon'),
    path('favorite-pokemon/pokemon-list/<int:pk>', views.single_pokemon_detail, name='single_pokemon_detail'),
    path('favorite-pokemon/pokemon-list/<int:pk>/edit', views.PokemonUpdateView.as_view(), name='pokemon_update'),
    path('favorite-pokemon/pokemon-list', views.pokemon_list, name='pokemon_list'),

]
