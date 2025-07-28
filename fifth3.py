#Write a function cosine_series(x, n) that takes an angle x in degrees and an integer n, and prints the sum of the first n terms of the cosine series expansion.
import math

def cos(x, n):
    x = math.radians(x)  # Convert degrees to radians
    result = 0
    for i in range(n):
        sign = (-1) ** i
        term = (x ** (2 * i)) / math.factorial(2 * i)
        result += sign * term
    return result

# Input from user
x = float(input("Enter the angle in degrees: "))
n = int(input("Enter the number of terms: "))

ans = cos(x, n)
print("The cosine value is:", ans)

