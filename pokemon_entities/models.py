from tkinter import CASCADE
from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название на русском')
    title_en = models.CharField(max_length=200, verbose_name='Название на английском')
    title_jp = models.CharField(max_length=200, verbose_name='Название на японском')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(blank=True, verbose_name='Картинка')
    previous_evolution = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='next_evolution',
        verbose_name='Из кого эволюционирует'
        )
    level = models.IntegerField(verbose_name='Уровень')
    health = models.IntegerField(verbose_name='Здоровье')
    strenght = models.IntegerField(verbose_name='Атака')
    defence = models.IntegerField(verbose_name='Защита')
    stamina = models.IntegerField(verbose_name='Выносливость')
    def __str__(self):
        return self.title
    
    
class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        verbose_name='Название покемона'
    )
    lat = models.FloatField(verbose_name='Широта на карте')
    lon = models.FloatField(verbose_name='Долгота на карте')
    appeared_at = models.DateTimeField(verbose_name='Когда покемон появится')
    disappeared_at = models.DateTimeField(verbose_name='Когда покемон исчезнет')
    def __str__(self):
        return f'{self.pokemon} находится по координатам: {self.lat}, {self.lon}'