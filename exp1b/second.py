#A program to find frequency of each digit in a given integer.

num = input("enter the number ")
for i in range(0, 9):
    for k in range(0,(len(num)-1)):
        if(int(num[k])==i):
            print(f"The count of {i} is {num.count(num[k])}")
        
