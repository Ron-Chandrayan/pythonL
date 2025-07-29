def factors():
  l=[]
  n = int(input("Enter a number: "))
  for i in range(1,n):
        if(n%i==0):
            l.append(i)
  return l
l1 = factors()
print(l1) 
