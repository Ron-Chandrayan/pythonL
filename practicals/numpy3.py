from numpy import *
arr1=arange(10)
print(arr1)
print(arr1.ndim)
arr1=arr1.reshape(2,5)
print(arr1)
print(arr1.shape)


arr2=array([[1,2,3],[4,5,6]])
print(arr2)

arr2=ones((3,4),int)
print(arr2)

print("hello")
arr3=reshape(arange(12),(2,3,2))