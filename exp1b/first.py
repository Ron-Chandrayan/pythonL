#A program to find all factors of a number.
num = int(input("Enter the number "))
print(f"the factors of {num} is \n")
for i in range(1,num+1):
    if(num%i==0):
        print(i," ")