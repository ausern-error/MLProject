from dataclasses import dataclass
@dataclass
class Vector2:
#placeholder, will be replaced when we decide on math library
    x: int
    y: int

@dataclass
class Entity:
    position: Vector2
    animal_type: str
    age: int
    max_age: int
    food: int
    food_consumption: int
    reproduction_rate: int
    days_since_reproduction: int
    children: list #TODO: Type annotate these
    parents: list
