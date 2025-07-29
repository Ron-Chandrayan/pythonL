import math 

def is_strong_number(num):
    total = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        factorial = math.factorial(digit)
        total += factorial
        temp //= 10
    return total == num
n =  int(input("Enter a number: "))
print(f"Strong numbers up to {n}:")
for i in range(1,n+1):
    if is_strong_number(i):
        print(i)
