#slicing

from numpy import *
a=arange(10,16)
print(a)
b=a[1:6:2]
print(b)
b=a[::]
print(b)
b=a[-2:2:-1]
print(b)
b=a[:-2:]
print(b)
