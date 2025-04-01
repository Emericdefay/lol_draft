from django.db import models

# models.py dans l'app 'draft'

from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Associe un joueur à un utilisateur
    champ_pool = models.ManyToManyField(Champion)  # Les champions disponibles pour le joueur

    def __str__(self):
        return self.user.username

class Archetype(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Champion(models.Model):
    TYPE_CHOICES = [
        ('Melee', 'Melee'),
        ('Range', 'Range'),
        ('Hybrid', 'Hybrid')
    ]

    name = models.CharField(max_length=100)
    image_url = models.URLField()  # URL vers l'image du champion
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    archetypes = models.ManyToManyField(Archetype)
    ap_ratio = models.FloatField()  # Ratio AP
    ad_ratio = models.FloatField()  # Ratio AD
    base_stats = models.JSONField()  # Statistiques de base du champion (hp, mana, etc.)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    players = models.ManyToManyField(Player)  # Les joueurs associés à l'équipe
    champions = models.ManyToManyField(Champion)  # Champions pickés dans l'équipe

    def __str__(self):
        return self.name


class DraftCondition(models.Model):
    description = models.TextField()
    condition_type = models.CharField(max_length=50)  # Exemple : "Counter Pick", "Combo"
    impact_on_draft = models.TextField()

    def __str__(self):
        return self.description
