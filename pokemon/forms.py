from django import forms

from .models import Pokemon

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ('name', 'types', 'text')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'text': forms.Textarea(attrs={'class': 'form-control mb-5'})
        }
        labels = {
            'text' : 'Write why this is one of your favorite pokemon! '
        }