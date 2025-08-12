#Write a Python program to get the largest and smallest number from a list 
number = int(input("Enter the number of elements: "))
l = []
for i in range(number):
    num = input(f"Enter element {i+1}: ")
    l.append(num)
print(f"Largest Element: {max(l)}")
print(f"Smallest Element: {min(l)}")