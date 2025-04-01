# admin.py dans l'app 'draft'

from django.contrib import admin
from .models import Champion, Player, Team, Archetype

@admin.register(Champion)
class ChampionAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'ap_ratio', 'ad_ratio')
    search_fields = ('name',)

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('user',)
    filter_horizontal = ('champ_pool',)  # Permet de gérer le champ pool via l'UI

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ('players', 'champions')  # Permet d'ajouter des joueurs et champions facilement

@admin.register(Archetype)
class ArchetypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
