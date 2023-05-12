from django.contrib import admin

from . import models


class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(models.Pokemon, PokemonAdmin)
