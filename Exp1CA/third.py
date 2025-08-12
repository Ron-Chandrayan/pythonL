#Count Vowels and Consonants

l =["a","e","i","o","u"]
d=0
c=0
str=input("enter the string ")
for i in str:
  if(i.lower() in l):
    c=c+1
  else:
    d=d+1
print("The number of vowels is ",c)
print("The number of consonants is ",d)