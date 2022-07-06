# Generated by Django 3.1.14 on 2022-07-06 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0005_auto_20220706_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='defence',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokemon',
            name='health',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokemon',
            name='level',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokemon',
            name='stamina',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokemon',
            name='strenght',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]
