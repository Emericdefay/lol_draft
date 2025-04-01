# draft/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Vue de draft principale, avec la sélection des champions
    path('draft/', views.draft_view, name='draft_view'),

    # Vue pour l'édition des joueurs et de leur champ pool
    path('player/<int:player_id>/', views.player_view, name='player_view'),

    # Vue pour afficher une équipe spécifique avec ses joueurs et champions
    path('team/<int:team_id>/', views.team_view, name='team_view'),

    # Vue d'administration pour gérer les drafts et les suggestions
    path('draft/suggestions/', views.suggest_pick_view, name='suggest_pick_view'),  # Vue qui donne des suggestions en fonction des picks
]
