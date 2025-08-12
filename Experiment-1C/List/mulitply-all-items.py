#Write a Python program to multiply all the items in a list 

number = int(input("Enter the number of elements: "))
l = []
for i in range(number):
    num = input(f"Enter element {i+1}: ")
    l.append(num)
product = 1
for i in l:
    product *= int(i)
print(product)
