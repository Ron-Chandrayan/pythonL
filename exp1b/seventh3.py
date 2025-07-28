#Write a Python function calculate_sine(x) that takes an angle x in degrees as input and returns its sine value. Use the math module for calculations.

import math

def calculate_sine(x):

    radians = math.radians(x)

    return math.sin(radians)


angle = float(input("Enter angle in degrees: "))
sine_value = calculate_sine(angle)
print(f"Sine of {angle}° is {sine_value:.6f}")
