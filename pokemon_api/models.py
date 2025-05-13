from django.db import models
from .services.score_service import ScoreService


class Pokemon(models.Model):
    pokemon_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    types = models.JSONField(blank=True, null=True)
    abilities = models.JSONField(blank=True, null=True)
    base_stats = models.JSONField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    image_url = models.URLField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} (#{self.pokemon_id})"

    def get_score(self):
        score_service = ScoreService()
        return score_service.calculate_score(self)
