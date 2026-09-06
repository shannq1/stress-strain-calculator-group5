def calculate_stress(force: float, area: float) -> float:
    if area == 0:
        raise ValueError("Area cannot be zero.")
    return force / area
