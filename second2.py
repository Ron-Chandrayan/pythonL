#A program to print all Strong numbers between 1 to n.
#A strong number is a positive integer where the sum of the factorials of its digits equals the number itself. 
import math
n= int(input("enter the terminal number "))
sum=0
for i in range(1,n+1):
    temp=i
    i=str(i)
    for k in range(0,len(i)):
        fact = math.factorial(int(i[k]))
        sum = sum+fact
    if(sum==temp):
        print(f"{temp} is a Strong number")
    else:
        pass
    sum=0


