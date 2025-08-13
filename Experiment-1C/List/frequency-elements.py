size1 = int(input("Enter number of elements in first list: "))
l1 = []

for i in range(size1):
    element1 = input(f"Enter element {i+1}: ")
    l1.append(element1)

size2 = int(input("Enter number of elements in first list: "))
l2 = []

for i in range(size2):
    element2 = input(f"Enter element {i+1}: ")
    l2.append(element1)

common = 0
for i in l1:
    if i in l2:
        common += 1
if common > 0:
    print(f"Number of common elements: {common}")
else:
    print("No common elements found.")