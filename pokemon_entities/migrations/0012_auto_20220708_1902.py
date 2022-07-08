# Generated by Django 3.1.14 on 2022-07-08 16:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0011_auto_20220708_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='defence',
            field=models.IntegerField(verbose_name='Защита'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='health',
            field=models.IntegerField(verbose_name='Здоровье'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='level',
            field=models.IntegerField(verbose_name='Уровень'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='previous_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='next_evolution', to='pokemon_entities.pokemon', verbose_name='Из кого эволюционирует'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='stamina',
            field=models.IntegerField(verbose_name='Выносливость'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='strenght',
            field=models.IntegerField(verbose_name='Атака'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название на русском'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_en',
            field=models.CharField(max_length=200, verbose_name='Название на английском'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(max_length=200, verbose_name='Название на японском'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(verbose_name='Когда покемон появится'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(verbose_name='Когда покемон исчезнет'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='lat',
            field=models.FloatField(verbose_name='Широта на карте'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='lon',
            field=models.FloatField(verbose_name='Долгота на карте'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.pokemon', verbose_name='Название покемона'),
        ),
    ]
