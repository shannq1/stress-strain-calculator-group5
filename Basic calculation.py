def get_valid_number(prompt, allow_zero=False):
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


def select_material():
    materials = {
        "1": {"name": "Steel", "yield_strength": 250, "youngs_modulus": 200},
        "2": {"name": "Aluminum", "yield_strength": 95, "youngs_modulus": 69},
        "3": {"name": "Titanium", "yield_strength": 880, "youngs_modulus": 114},
    }

    print("Select a material:")
    print("1. Steel")
    print("2. Aluminum")
    print("3. Titanium")
    print("4. Custom")

    while True:
        choice = input("Enter choice (1-4): ")

        if choice in materials:
            selected = materials[choice]
            print()
            print(f"Selected: {selected['name']}")
            print(f"Yield strength: {selected['yield_strength']} MPa")
            print(f"Young's modulus: {selected['youngs_modulus']} GPa")
            return selected

        elif choice == "4":
            name = input("Enter custom material name: ")
            yield_strength = get_valid_number("Enter yield strength (in MPa): ")
            youngs_modulus = get_valid_number("Enter Young's modulus (in GPa): ")
            return {"name": name, "yield_strength": yield_strength, "youngs_modulus": youngs_modulus}

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


def analyze_safety(stress_mpa, yield_strength):
    factor_of_safety = yield_strength / stress_mpa

    print()
    print("Safety Analysis:")
    print(f"Factor of safety: {factor_of_safety:.2f}")

    if factor_of_safety >= 2:
        print("SAFE - Material can handle this load comfortably.")
    elif factor_of_safety >= 1:
        print("CAUTION - Material is close to yield strength.")
    else:
        print("FAIL - Stress exceeds yield strength. Material will likely deform or break.")


def run_calculation():
    material = select_material()
    print()

    force = get_valid_number("Enter the force applied (in Newtons): ")
    area = get_valid_number("Enter the cross-sectional area (in square meters): ")
    original_length = get_valid_number("Enter the original length of the material (in meters): ")
    change_in_length = get_valid_number("Enter the change in length of the material (in meters): ", allow_zero=True)

    stress = force / area
    strain = change_in_length / original_length

    print()
    print("Results:")
    print()
    print(f"Stress: {stress:.2f} Pa")
    print(f"Strain: {strain:.5f} (dimensionless)")
    print()
    stress_mpa = stress / 1000000
    print(f"Stress in MPa: {stress_mpa:.2f} MPa")

    analyze_safety(stress_mpa, material["yield_strength"])

    return {
        "material": material["name"],
        "force": force,
        "area": area,
        "original_length": original_length,
        "change_in_length": change_in_length,
        "stress": stress,
        "stress_mpa": stress_mpa,
        "strain": strain,
        "factor_of_safety": analyze_safety(stress_mpa, material["yield_strength"])
    }

def main():
    #Main function for the stress and strain calculator with data structures.

    print("==Stress and Strain Calculator==")

    while True:
        print()
        run_calculation()

        print()
        again = input("Perform another calculation? (y/n): ").strip().lower()
        if again != "y":
            print()
            print("Thank you for using Group 5's Stress and Strain Calculator!")
            break


if __name__ == "__main__":
    main()