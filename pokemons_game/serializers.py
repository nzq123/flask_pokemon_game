from .models import PokemonModel, AbilityModel
from .pokemon import Pokemon, PokemonType
from .ability import Ability, AbilityType


def to_pokemon(model: PokemonModel) -> Pokemon:
    poke_types = []
    for i in model.type:
        poke_types.append(PokemonType(i.name.lower()))
    pokemon = Pokemon(name=model.name, damage=model.damage, max_hp=model.max_hp,
                      speed=model.speed, type=poke_types, trainer=None)
    return pokemon


def to_ability(model: AbilityModel) -> Ability:

    if model.type in AbilityType:
        ability = Ability(name=model.name, damage=model.damage, accuracy=model.accuracy, type=model.type, cooldown=0)
        return ability


