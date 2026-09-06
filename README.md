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


