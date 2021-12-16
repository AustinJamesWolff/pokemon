from flask import Flask, render_template 
from .models import DB, Pokemon
from .pokeapi import get_pokemon
import pprint

def create_app():

    # initialize flask app
    app = Flask(__name__)

    # Flask and SQLAlchemy configuration
    app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"

    # Connect our database toour app
    DB.init_app(app)

    # Make our root page
    @app.route("/")
    def root():
        return """<p>This is an example of getting Pikachu: 
         <br>testing multi lines
         <br>break.<p>"""

    @app.route("/pikachu")
    def pika():
        poke_name = 'pikachu'
        pokemon_data = get_pokemon(poke_name)['id']
        return str(pokemon_data)

    @app.route("/test")
    def test():
        poke_name = 'pikachu'
        pokemon_data = get_pokemon(poke_name)
        return pokemon_data

    # Usr the below to show the picture of the pokemon!
    @app.route("/<name>", methods=['GET'])
    def pic(name=None):
        name = name
        pokemon_data = get_pokemon(name)['sprites']['front_default']
        return '<img src=pokemon_data>'


    return app