from django.test import TestCase
from .models import Pokemon
from .forms import PokemonForm


class PokemonTestCase(TestCase):
    
    def create_pokemon(self,name="pikachu",types="electric",text=""):
        return Pokemon.objects.create(name=name,types=types,text=text)

    def test_model_str(self):
        """Should return True if name matches"""
        name = Pokemon.objects.create(name='pikachu')
        self.assertEqual(str(name), "pikachu")
    
    def test_pokemon_creation(self):
        """Should return true if pokemon exists"""
        p = self.create_pokemon()
        self.assertTrue(isinstance(p,Pokemon))
        self.assertEqual(p.__str__(), p.name)

    def test_invalid_form(self):
        """Should return true if text field is left blank."""
        p = Pokemon.objects.create(name="pikachu",types="electric",text="")
        data = {'name': p.name, "types": p.types, "text": p.text}
        form = PokemonForm(data=data)
        self.assertFalse(form.is_valid())
    
    def test_valid_form(self):
        """Should return true if all fields are filled."""
        p = Pokemon.objects.create(name="pikachu",types="electric",text="favorite pokemon")
        data = {'name': p.name, "types": p.types, "text": p.text}
        form = PokemonForm(data=data)
        self.assertTrue(form.is_valid())
