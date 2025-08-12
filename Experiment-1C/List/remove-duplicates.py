#Write a Python program to remove duplicates from a list
size = int(input("Enter number of elements in first list: "))
l1 = []

for i in range(size):
    element = input(f"Enter element {i+1}: ")
    l1.append(element)
print("List: ", l1)

l2 = []
for i in l1:
    if i not in l2:
        l2.append(i)
print("List (without duplicates): ", l2)