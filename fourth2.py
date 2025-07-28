#A program to find sum of all prime numbers between 1 to n.
num=int(input("enter the termination number "))
sum=0
for i in range(1,num+1):
    for k in range(1,i):
        if(i%k==0):
            sum=sum+k
    if(sum==1):
        print(f"{i} is a prime number")
    else:
        pass
    sum=0