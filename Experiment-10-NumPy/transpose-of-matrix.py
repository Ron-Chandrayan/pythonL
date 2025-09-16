from numpy import *
r,c=[int(a)for a in input("enter row and column:").split()]
str=input("enter matrix elements:\n")
x=reshape(matrix(str),(r,c))
print("original matrix is")
print(x)
print("transpose matrix is")
y=x.transpose()
print(y)