#A program to print all Perfect numbers between 1 to n.
num=int(input("enter the termination number "))
sum=0
for i in range(1,num+1):
    for k in range(1,i):
        if(i%k==0):
            sum=sum+k
    if(i==sum):
        print(f"{i} is perfect number")
    else:
        pass
    sum=0