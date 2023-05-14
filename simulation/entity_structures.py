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
class EntityManager():
    entities: list
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
    entity_manager: EntityManager

    def __post_init__(self):
        self.entity_manager.entities.append(self)
    def update_task(self):
        match self.task:
            case Task.wander:
                self.wander()
            case Task.gather:
                self.gather()
            case Task.reproduce:
                self.reproduce()
            case Task.hunt:
                self.hunt()
            case Task.escape:
                self.escape()
    def change_task(self,new_task):
        self.task = new_task
    def update(self):
        self.update_task()
        
    def wander(self):
        pass
    def gather(self):
        pass
    def reproduce(self):
        pass
    def hunt(self):
        pass
    def escape(self):
        pass
    
