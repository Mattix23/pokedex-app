from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, DetailView

import requests

from .models import Pokemon

class PokemonCreateView(CreateView):
    model = Pokemon
    fields = ['name', 'types', 'text']
    success_url = 'my-pokemon'

class PokemonSearchView(TemplateView):
    template_name = 'pokemon/pokemon_search.html'


def pokemon_detail(request):
    try:
        pokemon_name = request.GET.get('name')
        if not pokemon_name:
            return render(request, 'pokemon/search.html', {})

        response = requests.get(
            f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/')
        if response.status_code != 200:
            return render(request, 'pokemon/search.html', {'error_message:' f'Pokemon not found: {pokemon_name}'})

        data = response.json()
        name = data['name'].title()
        types = [t['type']['name'] for t in data['types']]
        height = data['height'] / 10  # Convert from decimeters to meters
        weight = data['weight'] / 10  # Convert from hectograms to kilograms
        sprite_url = data['sprites'].get('front_default')
        sprite_front = data['sprites'].get('front_default')
        sprite_back = data['sprites'].get('back_default')
        context = {
            'name': name,
            'types': types,
            'height': height,
            'weight': weight,
            'sprite_url': sprite_url,
            'sprite_front': sprite_front,
            'sprite_back': sprite_back,
        }
        return render(request, 'pokemon/pokemon_detail.html', context=context)
    except:
        return render(request, 'pokemon/error.html', {})


def pokemon_list(request):
    all_pokemon = Pokemon.objects.all()
    return render(request, 'pokemon/pokemon_list.html', {'pokemons': all_pokemon})


def single_pokemon_detail(request, pk):
    pokemon = Pokemon.objects.get(pk=pk)
    return render(request, 'pokemon/pokemon_single.html', {'pokemon': pokemon})