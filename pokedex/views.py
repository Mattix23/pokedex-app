from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

from datetime import datetime


class HomeView(TemplateView):
    template_name = 'pokedex/welcome.html'
    extra_context = {'today': datetime.today()}


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'pokedex/authorized.html'
    login_url = '/admin'

class LoginInterfaceView(LoginView):
    template_name = 'pokedex/login.html'

class LogoutInterfaceView(LogoutView):
    template_name = 'pokedex/logout.html'

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'pokedex/register.html'
    success_url = '/'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('pokedex_home')
        return super().get(request,*args,**kwargs)
