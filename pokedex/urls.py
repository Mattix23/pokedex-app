from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='pokedex_home'),
    # add new path to login here
]