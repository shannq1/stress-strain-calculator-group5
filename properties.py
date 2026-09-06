from dataclasses import dataclass


@dataclass
class MaterialProperties:
    yield_strength: float
    youngs_modulus: float