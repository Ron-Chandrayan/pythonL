# Write a Python program that: Asks the user to enter 10 integers
# Generates a dictionary where:
# Keys are the entered integers.
# Values are lists of all divisors of each integer (positive divisors only, regardless of input sign).

import math

dict={}

def factor(n):
    l=[]
    for i in range(1,n+1):
        if(n%i==0):
            l.append(i)
        else:
            pass
    return l

while(True):
    m=int(input("enter number "))
    key=m
    value=factor(abs(m))
    dict[key]=value
    c=int(input("press 1 to continue 2 to break "))
    if(c==1):
        pass
    else:
        break
print(dict)