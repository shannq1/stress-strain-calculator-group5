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

    def add_test_result(self, result_data: dict):
        """Appends a test result dictionary to the session history."""
        self.history.append(result_data)

    def get_highest_stress(self) -> float:
        """Calculates the highest stress value recorded in the session."""
        if not self.history:
            return 0.0
        return max(record.get("stress", 0.0) for record in self.history)

    def get_average_strain(self) -> float:
        """Calculates the average strain across all tests in the session."""
        if not self.history:
            return 0.0
        total_strain = sum(record.get("strain", 0.0) for record in self.history)
        return total_strain / len(self.history)
    def get_lowest_safety_factor(self) -> float:
        """Finds the lowest factor of safety recorded in the session."""
        if not self.history:
            return 0.0
        # Filters out records that might not have a safety factor calculated
        safety_factors = [record.get("safety_factor") for record in self.history if "safety_factor" in record]
        return min(safety_factors) if safety_factors else 0.0

    def export_to_json(self, filename: str = "session_history.json"):
        """Exports the session history to a JSON file."""
        import json
        with open(filename, "w") as file:
            json.dump(self.history, file, indent=4)
        print(f"Session history successfully exported to {filename}")
