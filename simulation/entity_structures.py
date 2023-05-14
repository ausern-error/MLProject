from dataclasses import dataclass
from enum import Enum
@dataclass
class Vector2:
#placeholder, will be replaced when we decide on math library
    x: int
    y: int

class Task(Enum):
    wander = 1
    gather = 2
    reproduce = 3
    hunt = 4
    escape = 5

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
    task: Task
    def wander():
        pass
    def gather():
        pass
    def reproduce():
        pass
    def hunt():
        pass
    def escape():
        pass
    
