from pokemons_game import app, db
from flask import render_template, redirect, url_for, request, jsonify
from pokemons_game.models import PokemonModel, TypeModel
from pokemons_game.pokemon import PokemonType
import json
import requests


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/pokemons')
def pokemons():
    return render_template('pokemons.html', pokemons=PokemonModel.query.all())


@app.route('/pokemon', methods=['GET', 'POST'])
def pokemon():
    if request.method == 'POST':
        body = request.get_json()
        # poke_types = []
        poke = PokemonModel(name=body['name'], damage=body['damage'], max_hp=body['max_hp'],
                            current_hp=body['max_hp'], speed=body['speed'],
                            type=TypeModel.query.filter(TypeModel.name.in_(body["type"])).all())
        db.session.add(poke)
        db.session.commit()
        return body
    if request.method == 'GET':
        tab = []
        for pokemon in PokemonModel.query.all():
            poke_types = []
            for i in pokemon.type:
                poke_types.append(PokemonType(i.name.lower()))
            pokemon = dict(id=pokemon.id, name=pokemon.name, damage=pokemon.damage, max_hp=pokemon.max_hp,
                           speed=pokemon.speed, type=poke_types, trainer=None)
            tab.append(pokemon)
        return tab


@app.route("/pokemon/<id_>",methods=["DELETE"])
def pokemon_delete(id_):
    pokemon = PokemonModel.query.get(id_)
    if pokemon is not None:
        db.session.delete(pokemon)
        db.session.commit()
    else:
        return "No pokemon with such ID"
    return "Pokemon was delete"


@app.route('/type_pokemon', methods=['GET', 'POST', 'DELETE'])
def type_pokemon():
    if request.method == 'POST':
        body = request.form
        type = TypeModel(name=body['name'])
        db.session.add(type)
        db.session.commit()
        return body
    if request.method == 'GET':
        tab = []
        for poke_type in TypeModel.query.all():
            poke_type = dict(id=poke_type.id, name=poke_type.name)
            tab.append(poke_type)
        return tab
    if request.method == 'DELETE':
        pass


@app.route("/type_pokemon/<id_>",methods=["DELETE"])
def type_pokemon_delete(id_):
    type_pokemon = TypeModel.query.get(id_)
    if type_pokemon is not None:
        db.session.delete(type_pokemon)
        db.session.commit()
    else:
        return "No type with such ID"
    return "Type was delete"


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    return redirect(url_for('market_page'))




