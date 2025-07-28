#A program to find power of a number using for loop.
base = int(input("Enter the base number"))
power = int(input("Enter the power"))
ans=1
for i in range(0,power):
    ans = ans*base
print("the ans is ",ans)