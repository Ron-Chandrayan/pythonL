#Write a Python program to print the numbers of a specified list after removing even numbers from it 

size = int(input("Enter number of elements in first list: "))
l1 = []

for i in range(size):
    element1 = int(input(f"Enter element {i+1}: "))
    l1.append(element1)

i = 0
while i < len(l1):
    if l1[i] % 2 == 0:  
        l1.pop(i)
    else:
        i += 1
print("List: ", l1)