#Write a Python program to check the first and last character are same from a given list of strings
li=list(eval(input("enter the list ")))
if(li[0][0]==li[-1][-1]):
    print("true")
else:
    print("false")