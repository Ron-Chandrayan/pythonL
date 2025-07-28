#Write a Python program to calculate the square root of a number input by the user. Use the assert statement to ensure that the input number is not negative, and print the square root only if the assertion passes.

import math

try:
    # Take input from user and convert to float
    num = float(input("Enter a number to find its square root: "))

    # Assert that the number is non-negative
    assert num >= 0, "Number must be non-negative."

    # Calculate and print the square root
    sqrt = math.sqrt(num)
    print(f"The square root of {num} is {sqrt:.4f}")

except AssertionError as e:
    print(f"AssertionError: {e}")

except ValueError:
    print("Invalid input! Please enter a valid number.")
