# Write a Python program to check the first and last character are same from a given list of strings 
num = int(input("Enter number of elements:"))
l = []
l = [input(f"Enter element {i+1}: ") for i in range(num)]

if(l[0][0] == l[-1][-1]):
  print(f"The first and last character are same: {l[0][0]}")
else:
  print(f"The first and last character are not same: {l[0][0]} and {l[-1][-1]}")  
