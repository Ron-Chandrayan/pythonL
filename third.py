#A program to find HCF (GCD) of two numbers.
num1 = int(input("enter the first number "))
num2 = int(input("enter the second number "))
l1=[]
l2=[]
for i in range(1,(num1+1)):
    if(num1%i==0):
        l1.append(i)

for i in range(1,(num2+1)):
    if(num2%i==0):
        l2.append(i)

l1= set(l1)
l2 = set(l2)
common = l1 & l2
common = list(common)
hcf = max(common)
print("the hcf is ",hcf)