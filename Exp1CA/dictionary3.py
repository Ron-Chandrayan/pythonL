# Write a Python program that:
# Asks the user to enter a positive integer n.
# Generates a dictionary where:
# Keys are integers from 1 to n.
# Values are the factorials of the corresponding keys (1!, 2!, ..., n!).

import math
dict={}
while(True):
    m=int(input("enter positive number "))
    if(m<0):
        print("negetive numbers not allowed ")
        break
    else:
        key=m
        value=math.factorial(m)
        dict[key]=value
    c=int(input("press 1 to continue 2 to break "))
    if(c==1):
        pass
    else:
        break
print(dict)