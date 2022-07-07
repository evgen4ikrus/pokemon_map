from tkinter import CASCADE
from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    title_jp = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(
        blank=True,
    )
    level = models.IntegerField()
    health = models.IntegerField()
    strenght = models.IntegerField()
    defence = models.IntegerField()
    stamina = models.IntegerField()
    def __str__(self):
        return self.title
    
    
class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
    )
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField()
    disappeared_at = models.DateTimeField()
    def __str__(self):
        return f'{self.pokemon} находится по координатам: {self.lat}, {self.lon}'