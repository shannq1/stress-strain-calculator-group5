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

class MaterialManager:

    def __init__(self):
        self._materials: Dict[str, Material] = {
            "1": Metal("Steel", 250, 200),
            "2": Metal("Aluminum", 95, 69),
            "3": Metal("Titanium", 880, 114),
        }

    def select_material(self) -> Material:
        print("Select a material:")
        print("1. Steel")
        print("2. Aluminum")
        print("3. Titanium")
        print("4. Custom")

        while True:
            choice = input("Enter choice (1-4): ")

            if choice in self._materials:
                selected = self._materials[choice]
                print()
                print(f"Selected: {selected.name}")
                print(f"Yield strength: {selected.yield_strength} MPa")
                print(f"Young's modulus: {selected.youngs_modulus} GPa")
                return selected

            elif choice == "4":
                name = input("Enter custom material name: ")
                yield_strength = InputValidator.get_valid_number("Enter yield strength (in MPa): ")
                youngs_modulus = InputValidator.get_valid_number("Enter Young's modulus (in GPa): ")
                return Composite(name, yield_strength, youngs_modulus)

            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")

class StressStrainTest:

    def __init__(self, material: Material, force: float, area: float, 
                 original_length: float, change_in_length: float):
        if area <= 0:
            raise ValueError("Cross-sectional area must be greater than zero.")
        if original_length <= 0:
            raise ValueError("Original length must be greater than zero.")

        self._material = material
        self._force = force
        self._area = area
        self._original_length = original_length
        self._change_in_length = change_in_length

