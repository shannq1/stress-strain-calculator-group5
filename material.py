from abc import ABC, abstractmethod
from dataclasses import dataclass
from properties import MaterialProperties


@dataclass
class Material(ABC):
    name: str
    properties: MaterialProperties

    @property
    def yield_strength(self) -> float:
        return self.properties.yield_strength

    @property
    def youngs_modulus(self) -> float:
        return self.properties.youngs_modulus

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
