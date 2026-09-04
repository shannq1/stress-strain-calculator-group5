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

    return factor_of_safety

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
    print("Calculation History:")
    if not history:
        print("No calculations were performed.")
    else:
        for i, record in enumerate(history, start=1):
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

    if history:
        stresses = [record['stress_mpa'] for record in history]
        fos_values = [record['factor_of_safety'] for record in history]
        strains = [record['strain'] for record in history]

        print()
        print("=== Statistics ===")
        print(f"Highest stress: {max(stresses):.2f} MPa")
        print(f"Lowest factor of safety: {min(fos_values):.2f}")
        print(f"Average strain: {sum(strains)/len(strains):.5f}")

        counts = {name: 0 for name in materials_tested}
        for r in history:
            counts[r['material']] += 1

        print("Material test counts:")
        for name, count in counts.items():
            print(f"  {name}: {count} test(s)")

        print()
        print("Thank you for using the Stress and Strain Calculator. Goodbye!")


if __name__ == "__main__":
    main()