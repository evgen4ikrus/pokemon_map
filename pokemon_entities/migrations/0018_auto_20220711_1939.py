# Generated by Django 3.1.14 on 2022-07-11 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0017_auto_20220711_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokemon_entitys', to='pokemon_entities.pokemon', verbose_name='Название покемона'),
        ),
    ]
