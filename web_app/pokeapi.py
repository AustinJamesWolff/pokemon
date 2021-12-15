import requests
import ast
import json
from .models import DB, Pokemon

def get_pokemon(pokemon_name):

    POKE_API_URL = "https://pokeapi.co/api/v2/pokemon/"

    # Make sure the returned name is lowercase
    pokemon_name = pokemon_name.lower()

    pokemon = json.loads(requests.get(
        POKE_API_URL + pokemon_name + "/").text)

    # try:
        # db_pokemon = Pokemon(id=pokemon['id'],
        #                      name= ,
        #                      ability=
        # )

        # DB.session.add()

    # except Exception as e:
    #     raise e

    # DB.session.commit()

    return pokemon