from flask import Flask, render_template 
from .models import DB
from .pokeapi import get_pokemon

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

    return app