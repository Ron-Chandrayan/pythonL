#Define a function factorial(n) that returns the factorial of a given number n
def factorial(n):
    sum=1
    for i in range(1,n+1):
        sum=sum*i
    return sum

a=int(input("enter the number of which u want the factorial "))
fact = factorial(a)
print("the factorial is ",fact)