def factors(n):
  l = []
  for i in range(1, n+1):
    if(n%i==0):
      l.append(i)
  return l
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
l1 = factors(num1)
l2 = factors(num2)
print(l1)
print(l2)
hcf = 1
for l in l1:
  if l in l2:
    hcf = l
print(f"HCF = {hcf}")