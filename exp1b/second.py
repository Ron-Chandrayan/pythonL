#A program to find frequency of each digit in a given integer.

def count_digit(n):
  d={}
  while(n>0):
    digit=n%10
    for i in range(0,10):
      if(digit==i):
        if(digit in d.keys()):
          d[digit]=d[digit]+1
        else:
          d[digit]=1
    n=n//10
  print(d)
n=int(input("enter the number "))
count_digit(n)
        
