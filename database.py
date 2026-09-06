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
      
