#Perform Mathematical Operations on arrays
from numpy import *
arr = array([10,20,30,40,50])

print("Original Array: ",arr)
print("After adding 5:", arr+5)
print("After subtracting 5:", arr-5)
print("After multiplying with 5:", arr*5)
print("After dividing with 5: ", arr/5)
print("After modulus with 5: ", arr%5)
print("Expression value: ", (arr+5)**2-10)
print("Sin values: ", sin(arr))
print("Cos values: ", cos(arr))
print("Tan values: ", tan(arr))
print("Biggest Value: ", max(arr))
print("Smallest Value: ", min(arr))
print("Sum of values of array: ", sum(arr))
print("Average of values of array: ", mean(arr))