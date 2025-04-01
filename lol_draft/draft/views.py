# views.py dans l'app 'draft'

from django.shortcuts import render
from .models import Team, Champion
from .utils import suggest_pick

def draft_view(request):
    # Exemple de récupération d'équipe et de champions
    team = Team.objects.get(id=request.GET.get('team_id'))
    enemy_team = Team.objects.get(id=request.GET.get('enemy_team_id'))

    suggestions = suggest_pick(team, enemy_team)

    return render(request, 'draft/draft_view.html', {'suggestions': suggestions})
