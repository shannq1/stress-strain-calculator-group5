def main():

    print("==Stress and Strain Calculator==")
    print()
    force = float(input("Enter the force applied (in Newtons): "))
    area = float(input("Enter the cross-sectional area (in square meters): "))

    original_length = float(input("Enter the original length of the material (in meters): "))
    change_in_length = float(input("Enter the change in length of the material (in meters): "))

    stress = force / area
    strain = change_in_length / original_length

    print()
    print("Results:")
    print()
    print(f"Stress: {stress:.2f} Pa")
    print(f"Strain: {strain:.2f} (dimensionless)")
    print()
    stress_mpa = stress / 1000000
    print(f"Stress in MPa: {stress_mpa:.2f} MPa")







