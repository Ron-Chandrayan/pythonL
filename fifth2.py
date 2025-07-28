#A program to print all Armstrong numbers between 1 to n.
num=int(input("enter termination "))
sum=0
for i in range(1,num+1):
    temp=i
    i=str(i)
    for k in range(0,len(i)):
        sum=sum+(int(i[k])**3)
    if(sum==temp):
        print(f"{temp} is an Armstrong number")
    else:
        pass
    sum=0
