#Define a function print_numbers(a, b) that takes two parameters a and b and prints all integers from a to b
def print_numbers(a,b):
    if(a<=b):
        for i in range(a,b+1):
            print(i, end=" ")
    else:
        print("invalid")
a= int(input("enter starting number"))
b = int(input("enter stopping number"))
print_numbers(a,b)