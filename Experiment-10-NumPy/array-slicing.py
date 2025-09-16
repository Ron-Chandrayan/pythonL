from numpy import *
a = arange(10,20)
print(a)

b = a[1:6:2]
print(b)

b = a[::] #copys either array to b
print(b)

b = a[-2:2:-1]
print(b)

b = a[:-2:]
print(b)