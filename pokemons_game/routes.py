from pokemons_game import app
from flask import render_template, redirect, url_for


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    return render_template('market.html')


@app.route('/register', methods=['GET', 'POST'])
def register_page():
        return redirect(url_for('market_page'))




