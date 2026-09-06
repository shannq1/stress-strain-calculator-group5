import json
import csv
import os
import random
from database import CalculatorSession


def main():
    print("==Stress and Strain Calculator==")
    session = CalculatorSession()

    while True:
        print()
        choice = input("Press Enter to run a calculator, 'r' for a random test, or 'q' to quit and see your summary: ").strip().lower()
        if choice == 'q':
            break
 
        try:
            if choice == 'r':
                test = session.run_random_calculation()
            else:
                test = session.run_calculation()
            session.history.append(test)
            session.materials_tested.add(test.material.name)

    while True:
        print()
        choice = input("Press Enter to run a calculator, or type 'q' to quit and see your summary: ").strip().lower()
        if choice == 'q':
            break

        try:
            test = session.run_calculation()
            session.history.append(test)
            session.materials_tested.add(test.material.name)

        except ValueError as e:
            print(f"Error: {e}")
        except ZeroDivisionError:
            print("Error: Area and original length cannot be zero!")
        except KeyError:
            print("Error: Material not found in database!")

    session.display_summary()
    print()
    print("Thank you for using the Stress and Strain Calculator. Goodbye!")


if __name__ == "__main__":
    main()
