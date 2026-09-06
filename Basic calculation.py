def calculate_stress(force: float, area: float) -> float:
    if area == 0:
        raise ValueError("Area cannot be zero.")
    return force / area

def calculate_strain(change_in_length: float, original_length: float) -> float:
    if original_length == 0:
        raise ValueError("Original length cannot be zero.")
    return change_in_length / original_length

def calculate_youngs_modulus(stress_pa: float, strain: float) -> float:
    if strain == 0:
        raise ValueError("Strain cannot be zero when calculating Young's modulus.")
    return stress_pa / strain

def calculate_factor_of_safety(yield_strength_mpa: float, stress_mpa: float) -> float:
    if stress_mpa == 0:
        return float('inf')
    return yield_strength_mpa / stress_mpa