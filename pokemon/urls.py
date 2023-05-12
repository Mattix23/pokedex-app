from django.urls import path

from . import views

urlpatterns = [
    path('', views.PokemonSearchView.as_view(), name='pokemon_search'),
    path('pokemon_detail/', views.pokemon_detail, name='pokemon_detail'),

]
