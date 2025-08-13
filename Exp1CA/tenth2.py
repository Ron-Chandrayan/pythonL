#Write a Python program to get the frequency of the elements in a list
li=list(eval(input("enter a list  ")))
freq={}
s=set(li)
l1=list(s)
for i in l1:
    freq[i]=li.count(i)
print(freq)