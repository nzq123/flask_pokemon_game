from pokemons_game import db, app

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


class PokemonModel(db.Model):
    __tablename__ = "pokemon"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    damage = db.Column(db.Integer(), nullable=False)
    max_hp = db.Column(db.Integer(), nullable=False)
    current_hp = db.Column(db.Integer(), nullable=False)
    speed = db.Column(db.Integer(), nullable=False)
    type = db.relationship('TypeModel', secondary=pokemon_types, primaryjoin=(pokemon_types.c.pokemon_id==id),backref='pokemons', lazy=True)
    abilities = db.relationship('AbilityModel', secondary=pokemon_abilities, primaryjoin=(pokemon_abilities.c.pokemon_id==id), backref='pokemons', lazy=True)

    def __repr__(self):
        return f'Pokemon {self.name}'


class TypeModel(db.Model):
    __tablename__ = "type"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)

    def __repr__(self):
        return f'Type of {self.name}'


class AbilityModel(db.Model):
    __tablename__ = "ability"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    damage = db.Column(db.Integer(), nullable=False)
    accuracy = db.Column(db.Integer(), nullable=False)
    type = db.Column(db.Integer, db.ForeignKey('type.id'), nullable=False)
    # type = db.relationship('TypeModel', backref='ability', lazy=True)

    def __repr__(self):
        return f'Ability {self.name}'


with app.app_context():
    db.create_all()

# AbilityModel.query.all().filter
