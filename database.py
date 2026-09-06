import json
from material import Material
from properties import StressStrainTest


class TestRecord:
    """Represents a single stress/strain calculation record."""
    def __init__(self, test_id: int, stress: float, strain: float, material: str = "Unknown"):
        self.test_id = test_id
        self.stress = stress
        self.strain = strain
        self.material = material

    def to_dict(self):
        """Converts the record to a dictionary format."""
        return {
            "test_id": self.test_id,
            "stress": self.stress,
            "strain": self.strain,
            "material": self.material
        }


class CalculatorSession:
    """Manages calculation history and session statistics."""
    def __init__(self):
        self.history = []
        self.materials_tested = set()  # Supports session.materials_tested in main.py

    def add_test_result(self, result_data: dict):
        """Appends a test result dictionary to the session history."""
        self.history.append(result_data)

    def run_calculation(self) -> StressStrainTest:
        """Prompts for input, performs calculations, and returns a test object for main.py."""
        print("\n--- New Calculation ---")
        material_name = input("Enter material name (Steel, Aluminum, Titanium): ").strip()

        preset_materials = {
            "steel": Material("Steel", yield_strength=250.0, ultimate_strength=400.0),
            "aluminum": Material("Aluminum", yield_strength=95.0, ultimate_strength=110.0),
            "titanium": Material("Titanium", yield_strength=880.0, ultimate_strength=950.0),
        }

        if material_name.lower() not in preset_materials:
            raise KeyError("Material not found in database!")

        selected_material = preset_materials[material_name.lower()]

        force = float(input("Enter Force (N): "))
        area = float(input("Enter Area (mm²): "))
        dL = float(input("Enter Change in Length (mm): "))
        L0 = float(input("Enter Original Length (mm): "))

        if area <= 0 or L0 <= 0:
            raise ZeroDivisionError("Area and original length cannot be zero!")

        test = StressStrainTest(
            force=force, 
            area=area, 
            change_in_length=dL, 
            original_length=L0, 
            material=selected_material
        )

        print(f"Calculated Stress: {test.calculate_stress():.2f} MPa")
        print(f"Calculated Strain: {test.calculate_strain():.4f}")

        return test

    def get_highest_stress(self) -> float:
        """Calculates the highest stress value recorded in the session."""
        if not self.history:
            return 0.0
        return max(
            getattr(item, "stress", item.get("stress", 0.0) if isinstance(item, dict) else 0.0)
            for item in self.history
        )

    def get_average_strain(self) -> float:
        """Calculates the average strain across all tests in the session."""
        if not self.history:
            return 0.0
        total_strain = sum(
            getattr(item, "strain", item.get("strain", 0.0) if isinstance(item, dict) else 0.0)
            for item in self.history
        )
        return total_strain / len(self.history)

    def get_lowest_safety_factor(self) -> float:
        """Finds the lowest factor of safety recorded in the session."""
        if not self.history:
            return 0.0
        safety_factors = []
        for item in self.history:
            sf = getattr(item, "safety_factor", item.get("safety_factor") if isinstance(item, dict) else None)
            if sf is not None:
                safety_factors.append(sf)
        return min(safety_factors) if safety_factors else 0.0

    def display_summary(self):
        """Displays formatted session summary statistics for main.py."""
        print("\n" + "=" * 30)
        print("      SESSION SUMMARY      ")
        print("=" * 30)
        print(f"Total Tests Performed: {len(self.history)}")
        print(f"Unique Materials Tested: {', '.join(self.materials_tested) if self.materials_tested else 'None'}")
        print(f"Highest Stress Recorded: {self.get_highest_stress():.2f} MPa")
        print(f"Average Strain Recorded: {self.get_average_strain():.4f}")

    def export_to_json(self, filename: str = "session_history.json"):
        """Exports the session history to a JSON file."""
        records = []
        for item in self.history:
            if hasattr(item, "to_dict"):
                records.append(item.to_dict())
            elif isinstance(item, dict):
                records.append(item)
            else:
                records.append(vars(item))

        with open(filename, "w") as file:
            json.dump(records, file, indent=4)
        print(f"Session history successfully exported to {filename}")
