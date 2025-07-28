#Design a Python program with a function to check if a list contains negative numbers. If a negative number is found, use the pass statement to ignore it and continue checking the rest of the list. Finally, print the count of positive numbers.
l=eval(input("enter a list "))
c=0
for i in l:
    if(i<0):
        pass
    elif(i>=0):
        c=c+1
print(f"the count of positive numbers in a list is {c}")