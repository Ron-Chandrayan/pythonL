from numpy import *
r,c=[int(a) for a in input("enter rows and columns :").split()]
str=input("Enter matrix elements: \n")
x=reshape(matrix(str),(r,c))
print("original matrix is")
print(x)
print("transpose of matrix ")
y=x.transpose()
print(y)