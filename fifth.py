#A program to find LCM of two numbers.
#lcm (a*b)/gcd(a,b)
import math
a=int(input("enter the first number "))
b=int(input("enter the second number "))
lcm = (a*b)/(math.gcd(a,b))
print(f"The lcm is {lcm}")
