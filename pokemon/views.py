from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, UpdateView, ListView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

import requests

from .forms import PokemonForm
from .models import Pokemon

class PokemonDeleteView(LoginRequiredMixin,DeleteView):
    model = Pokemon
    success_url = "/"
    template_name = 'pokemon/pokemon_delete.html'
    login_url = "/login"

class PokemonUpdateView(LoginRequiredMixin,UpdateView):
    model = Pokemon
    success_url = "/"
    form_class = PokemonForm
    login_url = "/login"

class PokemonCreateView(LoginRequiredMixin,CreateView):
    model = Pokemon
    success_url = 'pokemon-list'
    form_class = PokemonForm
    login_url = "/login"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class PokemonSearchView(TemplateView):
    template_name = 'pokemon/pokemon_search.html'


class PokemonListView(LoginRequiredMixin, ListView):
    model = Pokemon
    context_object_name = "pokemons"
    template_name = "pokemon/pokemon_list.html"
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.pokemon.all()

def pokemon_detail(request):
    try:
        pokemon_name = request.GET.get('name')
        if not pokemon_name:
            return render(request, 'pokemon/search.html', {})

        response = requests.get(
            f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/', allow_redirects=False)
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


def single_pokemon_detail(request, pk):
    pokemon = Pokemon.objects.get(pk=pk)
    return render(request, 'pokemon/pokemon_single.html', {'pokemon': pokemon})