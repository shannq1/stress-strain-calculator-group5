# Stress and Strain Analysis System

## Project Description

This program is a Python-based Stress and Strain Analysis System developed for an engineering
programming course. It began as a basic calculator computing stress and strain from user input
and evolved through six stages into a modular, object-oriented application. The system helps
users calculate stress and strain for a given material, checks whether the calculated stress is
safe relative to the material's yield strength, and tracks a full session of test results with
summary statistics.

## Group Members

| Member | Primary Responsibility |

Marc Ira Irabagon | Task 1 – Basic Calculations 

Philip Shan Gallego | Task 2 – Control Structures and Validation 

Abdullaziz Macalalad | Task 3 – Data Structures 

Arwin Abad | Task 4 – Functions and Parameters 

Gabriel Ponce Agmata | Task 5 – Object-Oriented Programming 

**Task 6 – Modular Integration** was completed collaboratively by all five members.

## Program Features

- Calculates stress (σ = F / A) and strain (ε = ΔL / L₀) from user-provided measurements
- Validates all numeric input, rejecting non-numeric, negative, and invalid zero values without crashing
- Material selection menu with built-in properties for Steel, Aluminum, and Titanium, plus support for custom materials
- Safety analysis comparing calculated stress against the selected material's yield strength, with a factor of safety calculation and SAFE / CAUTION / FAIL verdict
- Tracks a full session's calculation history, including unique materials tested and summary statistics (highest stress, lowest factor of safety, average strain)
- Object-oriented material hierarchy (Metal, Plastic, Composite) supporting comparison and analysis across multiple materials and tests

## Installation / Requirements

- Python 3.10 or higher (uses dataclasses, type hints, and abstract base classes)
- No external/third-party packages required, uses only the Python standard library

## How to Run

1. Open a terminal or command prompt and navigate to the project's root directory.
2. Execute the main application file using Python: python main.py
3. Follow the interactive command-line menu to input your test measurements, select materials, and view the calculated stress, strain, and safety margins.

## Repository Structure

- main.py: The primary entry point containing the interactive user loop and menu navigation.
- material.py: Contains the object-oriented definitions, including the core Material class.
- properties.py: Houses the engineering calculations, including the StressStrainTest class logic.
- database.py: Manages the CalculatorSession class to track test history and compute session statistics.
- utils.py: Provides helper tools and validation functions to handle user input errors safely.
- tests.py: The comprehensive unit test suite used to verify the program's classes and calculations.

## Testing Requirements

The system relies entirely on Python's built-in unittest framework, meaning no external 
dependencies are required to validate the code. You can execute the full suite by running 
python tests.py in your terminal.

- TestMaterial: Validates the proper initialization of material objects and ensures all core attributes are accurately assigned.
- TestStressStrainTest: Confirms the mathematical precision of the stress and strain formulas while verifying that invalid inputs, such as a zero-value area, correctly trigger a ValueError.
- TestCalculatorSession: Checks that the session history accurately logs individual test results and successfully retains multiple calculation records over time.
