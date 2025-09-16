#Write a Python program to print the numbers of a specified list after removing even numbers from it
li=list(eval(input("enter the list  ")))
s=set(li)
li=list(s)
for i in li:
    if(i%2==0):
        li.pop(li.index(i))
print(li)