from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, List, Set, Tuple


@dataclass
class Material(ABC):
    name: str
    yield_strength: float
    youngs_modulus: float

    @abstractmethod
    def category(self) -> str:
        pass


@dataclass
class Metal(Material):
    def category(self) -> str:
        return "Metal"


@dataclass
class Plastic(Material):
    def category(self) -> str:
        return "Plastic"


@dataclass
class Composite(Material):
    def category(self) -> str:
        return "Composite"

