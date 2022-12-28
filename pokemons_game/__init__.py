import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pokemons_game.db'
app.config['SECRET_KEY'] = '07496568ab2b186aeb2dde41'
db = SQLAlchemy(app)
from pokemons_game import routes
from pokemons_game.serializers import to_pokemon, to_ability
from pokemons_game.models import PokemonModel, TypeModel, AbilityModel

