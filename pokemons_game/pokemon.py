from __future__ import annotations
from typing import List
from enum import Enum
from .ability import Ability


class PokemonType(str, Enum):
    WATER = "water"
    FIRE = "fire"
    GRASS = "grass"
    ICE = "ice"
    GROUND = "ground"
    POISON = "poison"


class Pokemon:
    def __init__(self, name: str, damage: float, max_hp: float, speed: float, type: List[PokemonType], trainer: None):
        self.name = name
        self.damage = damage
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.speed = speed
        self.type = type
        self.trainer = trainer
        self.abilities: List[Ability] = []