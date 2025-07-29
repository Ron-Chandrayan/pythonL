import math 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
def cosine_maclaurin_series(x, n_terms):
    cos_approx =0
    for n in range(n_terms):
        term = ((-1) ** n) * (x ** (2 * n)) / factorial(2 * n)
        cos_approx += term
    return cos_approx
x = float(input("Enter the value of x (in radians): "))
n_terms = int(input("Enter the number of terms in the series: "))
approx = cosine_maclaurin_series(x, n_terms)
actual = math.cos(x)
print(f"Approximated cos{x} with {n_terms} terms: {approx}")   
print(f"Actual cos({x}) using math.cos:{actual}")
print(f"Difference: {abs(actual - approx)}")