from dataclasses import dataclass
@dataclass

class Vector2:
#placeholder, will be replaced when we decide on math library
	x: int
	y: int

@dataclass
class Entity:
	position: Vector2
