from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название на русском')
    title_en = models.CharField(max_length=200, verbose_name='Название на английском', blank=True)
    title_jp = models.CharField(max_length=200, verbose_name='Название на японском', blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    image = models.ImageField(verbose_name='Картинка', blank=True, null=True)
    previous_evolution = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='next_evolution',
        verbose_name='Из кого эволюционирует'
        )
    
    level = models.IntegerField(verbose_name='Уровень', null=True, blank=True)
    health = models.IntegerField(verbose_name='Здоровье', null=True, blank=True)
    strenght = models.IntegerField(verbose_name='Атака', null=True, blank=True)
    defence = models.IntegerField(verbose_name='Защита', null=True, blank=True)
    stamina = models.IntegerField(verbose_name='Выносливость', null=True, blank=True)
    
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
    appeared_at = models.DateTimeField(verbose_name='Когда покемон появится', null=True, blank=True)
    disappeared_at = models.DateTimeField(verbose_name='Когда покемон исчезнет', null=True, blank=True)
    
    def __str__(self):
        return f'{self.pokemon} находится по координатам: {self.lat}, {self.lon}'