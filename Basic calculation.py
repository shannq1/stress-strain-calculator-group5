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

def get_valid_number(prompt: str, allow_zero: bool = False) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Value cannot be negative. Please try again.") 
            elif value == 0 and not allow_zero:
                print("Value cannot be zero. Please try again.") 
            else:
                return value #[cite: 1, 3]
        except ValueError:
            print("Please enter a valid number.") 

def manage_materials() -> dict:
    return {
        "1": {"name": "Steel", "yield_strength": 250, "youngs_modulus": 200},
        "2": {"name": "Aluminum", "yield_strength": 95, "youngs_modulus": 69},
        "3": {"name": "Titanium", "yield_strength": 880, "youngs_modulus": 114},
        }

def select_material() -> dict:
    materials = manage_materials()
    print("\nSelect a material:\n1. Steel\n2. Aluminum\n3. Titanium\n4. Custom")
    
    while True:
        choice = input("Enter choice (1-4): ") 
        if choice in materials:
            return materials[choice]
        elif choice == "4":
            return {
                "name": input("Enter custom material name: "), 
                "yield_strength": get_valid_number("Enter yield strength (in MPa): "), 
                "youngs_modulus": get_valid_number("Enter Young's modulus (in GPa): ") 
            }
        print("Invalid choice. Please enter 1, 2, 3, or 4.") 
        
        
def display_safety_analysis(factor_of_safety: float):
    print(f"\nSafety Analysis:\nFactor of safety: {factor_of_safety:.2f}") 
    if factor_of_safety >= 2:
        print("SAFE - Material can handle this load comfortably.") 
    elif factor_of_safety >= 1:
        print("CAUTION - Material is close to yield strength.") 
    else:
        print("FAIL - Stress exceeds yield strength. Material will likely deform or break.") 

def display_summary(history: list, unique_materials: set):
    print("\n=== Session Summary ===")
    print(f"Total calculations performed: {len(history)}")
    print(f"Unique materials tested: {', '.join(unique_materials) if unique_materials else 'None'}")
    
    if history:
        stresses = [r['stress_mpa'] for r in history]
        fos_values = [r['factor_of_safety'] for r in history]
        
        print("\n=== Statistics ===")
        print(f"Highest stress: {max(stresses):.2f} MPa")
        print(f"Lowest factor of safety: {min(fos_values):.2f}")
        
def run_calculation_record(units: tuple) -> dict:
    force_unit, area_unit, length_unit = units
    material = select_material()
    
    force = get_valid_number(f"\nEnter the force applied (in {force_unit}): ")
    area = get_valid_number(f"Enter the cross-sectional area (in {area_unit}): ")
    original_length = get_valid_number(f"Enter the original length (in {length_unit}): ")
    change_in_length = get_valid_number(f"Enter the change in length (in {length_unit}): ", allow_zero=True)
    
    stress_pa = calculate_stress(force, area)
    strain = calculate_strain(change_in_length, original_length)
    stress_mpa = stress_pa / 1_000_000
    fos = calculate_factor_of_safety(material["yield_strength"], stress_mpa)
    
    print(f"\nResults:\nStress: {stress_pa:.2f} Pa ({stress_mpa:.2f} MPa)")
    print(f"Strain: {strain:.5f} (dimensionless)")
    display_safety_analysis(fos)
    
    return {
        "material": material["name"],
        "force": force, "area": area,
        "stress_mpa": stress_mpa, "strain": strain,
        "factor_of_safety": fos
    }

def main():
    print("==Stress and Strain Calculator==") 
    units = ("Newtons", "square meters", "meters")
    history = []
    materials_tested = set()
    
    while True:
        choice = input("\nPress Enter to run a calculator, or type 'q' to quit: ").strip().lower() #[cite: 3]
        if choice == 'q': 
            break 
        try:
            record = run_calculation_record(units)
            history.append(record)
            materials_tested.add(record["material"])
        except ValueError as e:
            print(f"Error: {e}")
            
    display_summary(history, materials_tested)

if __name__ == "__main__":
    main()