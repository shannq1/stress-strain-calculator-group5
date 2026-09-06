def calculate_stress(force: float, area: float) -> float:
    if area == 0:
        raise ValueError("Area cannot be zero.")
    return force / area

def calculate_strain(change_in_length: float, original_length: float) -> float:
    if original_length == 0:
        raise ValueError("Original length cannot be zero.")
    return change_in_length / original_length
