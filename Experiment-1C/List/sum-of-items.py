# Write a Python program to sum all the items 

number = int(input("Enter the number of elements: "))
l = []
for i in range(number):
    num = input(f"Enter element {i+1}: ")
    l.append(num)
sum = 0
for i in l:
    sum += int(i)
print(sum)