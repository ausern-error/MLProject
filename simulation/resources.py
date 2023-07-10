import simulation.entity_structures
from dataclasses import dataclass

@dataclass
class Resource:
    texture_name: str
    name: str


@dataclass
class AnimalResourceRequirements:
    neededForSurvival: bool
    neededForReproduction: bool
    priority: int #animals who have multiple requirements will go to the closest resource with the highest priority
    dailyUsageRate: list # rate is randomly chosen from list, TODO: Investigate weighting this
    reproductionUsageRate: list
