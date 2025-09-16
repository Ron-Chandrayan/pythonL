#Write a Program that get two lists as input and check if they have at least one common member
li=list(eval(input("enter the list 1 ")))
li2=list(eval(input("enter the list 2 ")))
s1=set(li)
s2=set(li2)
s3=s1 & s2
l3=list(s3)
if(len(l3)>0):
    print("common element exists")
else:
    print("common element doesnt exists")