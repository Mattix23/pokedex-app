from django.contrib import admin

from . import models


class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name', 'text')


admin.site.register(models.Pokemon, PokemonAdmin)
