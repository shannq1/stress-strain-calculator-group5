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

    @property
    def material(self) -> Material:
        return self._material

    @property
    def force(self) -> float:
        return self._force

    @property
    def area(self) -> float:
        return self._area

    @property
    def original_length(self) -> float:
        return self._original_length

    @property
    def change_in_length(self) -> float:
        return self._change_in_length

    @property
    def stress(self) -> float:
        return self._force / self._area

    @property
    def stress_mpa(self) -> float:
        return self.stress / 1_000_000

    @property
    def strain(self) -> float:
        return self._change_in_length / self._original_length

    @property
    def factor_of_safety(self) -> float:
        if self.stress_mpa <= 0:
            return float('inf')
        return self.material.yield_strength / self.stress_mpa

    def analyze_safety(self) -> float:
        fos = self.factor_of_safety
        print()
        print("Safety Analysis:")
        print(f"Factor of safety: {fos:.2f}")

        if fos >= 2:
            print("SAFE - Material can handle this load comfortably.")
        elif fos >= 1:
            print("CAUTION - Material is close to yield strength.")
        else:
            print("FAIL - Stress exceeds yield strength. Material will likely deform or break.")

        return fos

    def display_results(self):
        print()
        print("Results:")
        print()
        print(f"Stress: {self.stress:.2f} Pa")
        print(f"Strain: {self.strain:.5f} (dimensionless)")
        print()
        print(f"Stress in MPa: {self.stress_mpa:.2f} MPa")
        self.analyze_safety()

    def to_dict(self) -> dict:
        return {
            "material": self.material.name,
            "force": self.force,
            "area": self.area,
            "original_length": self.original_length,
            "change_in_length": self.change_in_length,
            "stress": self.stress,
            "stress_mpa": self.stress_mpa,
            "strain": self.strain,
            "factor_of_safety": self.factor_of_safety
        }

class CalculatorSession:

    def __init__(self):
        self.history: List[StressStrainTest] = []
        self.materials_tested: Set[str] = set()
        self.material_manager = MaterialManager()

    def run_calculation(self) -> StressStrainTest:
        material = self.material_manager.select_material()
        print()

        force = InputValidator.get_valid_number("Enter the force applied (in Newtons): ")
        area = InputValidator.get_valid_number("Enter the cross-sectional area (in square meters): ")
        original_length = InputValidator.get_valid_number("Enter the original length of the material (in meters): ")
        change_in_length = InputValidator.get_valid_number("Enter the change in length of the material (in meters): ", allow_zero=True)

        test = StressStrainTest(material, force, area, original_length, change_in_length)
        test.display_results()
        return test

    def display_summary(self):
        print()
        print("=== Session Summary ===")
        print(f"Total calculations performed: {len(self.history)}")
        print(f"Unique materials tested: {', '.join(self.materials_tested) if self.materials_tested else 'None'}")

        print()
        print("Calculation History:")
        if not self.history:
            print("No calculations were performed.")
        else:
            for i, test in enumerate(self.history, start=1):
                record = test.to_dict()
                print(f"Calculation {i}:")
                print(f"  Material: {record['material']}")
                print(f"  Force: {record['force']} N")
                print(f"  Area: {record['area']} m^2")
                print(f"  Original Length: {record['original_length']} m")
                print(f"  Change in Length: {record['change_in_length']} m")
                print(f"  Stress: {record['stress']:.2f} Pa ({record['stress_mpa']:.2f} MPa)")
                print(f"  Strain: {record['strain']:.5f}")
                print(f"  Factor of Safety: {record['factor_of_safety']:.2f}")
                print()

        if self.history:
            stresses = [test.stress_mpa for test in self.history]
            fos_values = [test.factor_of_safety for test in self.history]
            strains = [test.strain for test in self.history]

            print()
            print("=== Statistics ===")
            print(f"Highest stress: {max(stresses):.2f} MPa")
            print(f"Lowest factor of safety: {min(fos_values):.2f}")
            print(f"Average strain: {sum(strains)/len(strains):.5f}")

            counts = {name: 0 for name in self.materials_tested}
            for test in self.history:
                counts[test.material.name] += 1

            print("Material test counts:")
            for name, count in counts.items():
                print(f"  {name}: {count} test(s)")

def main():
    print("==Stress and Strain Calculator==")
    session = CalculatorSession()

    while True:
        print()
        choice = input("Press Enter to run a calculator, or type 'q' to quit and see your summary: ").strip().lower()
        if choice == 'q':
            break

        try:
            test = session.run_calculation()
            session.history.append(test)
            session.materials_tested.add(test.material.name)

        except ValueError as e:
            print(f"Error: {e}")
        except ZeroDivisionError:
            print("Error: Area and original length cannot be zero!")
        except KeyError:
            print("Error: Material not found in database!")

    session.display_summary()
    print()
    print("Thank you for using the Stress and Strain Calculator. Goodbye!")


if __name__ == "__main__":
    main()