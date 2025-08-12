#Write a Python program to check a list is empty or not

size1 = int(input("Enter number of elements in first list: "))
l1 = []

for i in range(size1):
    element1 = input(f"Enter element {i+1}: ")
    l1.append(element1)

if len(l1) == 0:
  print("List is empty")
else:
  print("List is not empty")