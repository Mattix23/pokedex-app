from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from datetime import datetime


class HomeView(TemplateView):
    template_name = 'pokedex/welcome.html'
    extra_context = {'today': datetime.today()}


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'pokedex/authorized.html'
    login_url = '/admin'
