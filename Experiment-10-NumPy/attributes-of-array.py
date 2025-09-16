#attributes of array
from numpy import *
arr1 = array([[1,2,3],[4,5,6]])
print(arr1)
print("\n")

a3 = array([[[1,2,3,4],[5,6,7,8],[8,9,10,11]],[[1,2,3,4],[5,6,7,8],[8,9,10,11]]])
print(a3)
print(arr1.ndim)
print(arr1.shape)
print(a3.shape)
print(a3.ndim)

a3[1][2]