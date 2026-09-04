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


def main():

    print("==Stress and Strain Calculator==")
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
    print(f"Strain: {strain:.2f} (dimensionless)")
    print()
    stress_mpa = stress / 1000000
    print(f"Stress in MPa: {stress_mpa:.2f} MPa")


if __name__ == "__main__":
    main()