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

class InputValidator:

    @staticmethod
    def get_valid_number(prompt: str, allow_zero: bool = False) -> float:
        while True:
            try:
                value = float(input(prompt))
                if value < 0:
                    print("Value cannot be negative. Please try again.")
                elif value == 0 and not allow_zero:
                    print("Value cannot be zero. Please try again.")
                else:
                    return value
            except ValueError:
                print("Please enter a valid number.")

