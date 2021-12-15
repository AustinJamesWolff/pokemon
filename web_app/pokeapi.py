import requests
import ast

def get_pokemon(pokemon_name):

    POKE_API_URL = "https://pokeapi.co/api/v2/pokemon/"

    # literal_eval turns JSON into python dictionary
    pokemon = ast.literal_eval(requests.get(POKE_API_URL + pokemon_name).text)

    return pokemon