from pokemons_game import db, app

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Item', backref='owned_user', lazy=True)

    def __repr__(self):
        return f'User {self.username}'


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Item {self.name}'


pokemon_abilities = db.Table(
    "pokemon_abilities",
    db.Column("pokemon_id", db.Integer, db.ForeignKey("pokemon.id")),
    db.Column("ability_id", db.Integer, db.ForeignKey("ability.id")),
)

pokemon_types = db.Table(
    "pokemon_types",
    db.Column("pokemon_id", db.Integer, db.ForeignKey("pokemon.id")),
    db.Column("type_id", db.Integer, db.ForeignKey("type.id")),
)


class Pokemon(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    damage = db.Column(db.Integer(), nullable=False)
    max_hp = db.Column(db.Integer(), nullable=False)
    current_hp = db.Column(db.Integer(), nullable=False)
    speed = db.Column(db.Integer(), nullable=False)
    type = db.relationship('Type', secondary=pokemon_types, primaryjoin=(pokemon_types.c.pokemon_id==id),backref='pokemons', lazy=True)
    abilities = db.relationship('Ability', secondary=pokemon_abilities, primaryjoin=(pokemon_abilities.c.pokemon_id==id), backref='pokemons', lazy=True)

    def __repr__(self):
        return f'Pokemon {self.name}'


class Type(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)


class Ability(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    damage = db.Column(db.Integer(), nullable=False)
    accuracy = db.Column(db.Integer(), nullable=False)
    type = db.Column(db.Integer, db.ForeignKey('type.id'), nullable=False)


with app.app_context():
    db.create_all()

