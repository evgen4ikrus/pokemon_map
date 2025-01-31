import folium
from django.shortcuts import render
from django.utils.timezone import localtime
from django.urls import reverse
from pogomap.settings import MEDIA_URL

from .models import Pokemon, PokemonEntity

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    now = localtime()
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemon_entities = PokemonEntity.objects.filter(
        appeared_at__lte=now,
        disappeared_at__gte=now,
        )
    
    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            request.build_absolute_uri(f'{MEDIA_URL}{pokemon_entity.pokemon.image}')
        )

    pokemons = Pokemon.objects.all()
    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': request.build_absolute_uri(f'{MEDIA_URL}{pokemon.image}'),
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    now = localtime()
    pokemon = Pokemon.objects.get(id=pokemon_id)
    pokemon_entities = pokemon.entities.filter(
        appeared_at__lte=now,
        disappeared_at__gte=now,
        )
    pokemon_next_evolution = pokemon.next_evolutions.filter().first()
    pokemon_previous_evolution = pokemon.previous_evolution

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.lon,
            request.build_absolute_uri(f'{MEDIA_URL}{pokemon_entity.pokemon.image}')
        )

    pokemon_serialized = {
        'title_ru': pokemon.title,
        'img_url': request.build_absolute_uri(f'{MEDIA_URL}{pokemon.image}'),
        'description': pokemon.description,
        'title_en': pokemon.title_en,
        'title_jp': pokemon.title_jp,
    }

    if pokemon_previous_evolution:
        pokemon_serialized['previous_evolution'] = {
            'title_ru': pokemon_previous_evolution.title,
            'pokemon_id': pokemon_previous_evolution.id,
            'img_url': request.build_absolute_uri(f'{MEDIA_URL}{pokemon_previous_evolution.image}'),
        }

    if pokemon_next_evolution:
        pokemon_serialized['next_evolution'] = {
            'title_ru': pokemon_next_evolution.title,
            'pokemon_id': pokemon_next_evolution.id,
            'img_url': request.build_absolute_uri(f'{MEDIA_URL}{pokemon_next_evolution.image}'),
        }

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon_serialized
    })
