#this file serves as a utility module for the main program.

PASCALS_PER_MPA = 1_000_000

#core calculations

def calculate_stress(force: float, area: float) -> float:
    if area <= 0:
        raise ValueError("Cross-sectional area must be greater than zero.")
    return force / area


def calculate_strain(change_in_length: float, original_length: float) -> float:
    if original_length <= 0:
        raise ValueError("Original length must be greater than zero.")
    return change_in_length / original_length


def calculate_factor_of_safety(yield_strength_mpa: float, stress_mpa: float) -> float:
    if stress_mpa <= 0:
        return float('inf')
    return yield_strength_mpa / stress_mpa


def classify_safety(factor_of_safety: float) -> str:
    if factor_of_safety >= 2:
        return "SAFE - Material can handle this load comfortably."
    elif factor_of_safety >= 1:
        return "CAUTION - Material is close to yield strength."
    else:
        return "FAIL - Stress exceeds yield strength. Material will likely deform or break."


#conversion utilities

def pascals_to_megapascals(stress_pa: float) -> float:
    return stress_pa / PASCALS_PER_MPA


def megapascals_to_pascals(stress_mpa: float) -> float:
    return stress_mpa * PASCALS_PER_MPA


#user input validation

class InputValidator:
    #utilities to verify/double check user input for errors.

    @staticmethod
    def get_valid_number(prompt: str, allow_zero: bool = False) -> float:
        #this method asks user for a number and keeps asking until they give a valid one.
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