import math

def calculate_sine(x):

    radians = math.radians(x)

    return math.sin(radians)


angle = float(input("Enter angle in degrees: "))
sine_value = calculate_sine(angle)
print(f"Sine of {angle}° is {sine_value:.6f}")