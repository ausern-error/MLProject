import entity_structures
from dataclasses import dataclass

@dataclass
class Resource:
    Sprite: None #   uncomment after we have a way of rendering sprites
    Name: str


@dataclass
class AnimalResourceRequirements:
    neededForSurvival: bool
    neededForReproduction: bool
    priority: int #animals who have multiple requirements will go to the closest resource with the highest priority
    dailyUsageRate: list # rate is randomly chosen from list, TODO: Investigate weighting this
    reproductionUsageRate: list
