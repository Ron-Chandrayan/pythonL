import numpy as np
a5 = np.array([[1,2,3,4],[5,6,7,8],[8,9,10,11],[12,13,14,15],[80,90,100,120],[85,93,11,11]])

print(a5)
a5[-2:] #fetch last two rows
a5[1:3]
a5[1:] #print all rows except for the 1st roww
a5[1:,2] #printing second last element from each row
a5[0:,(1,2)]

#reshape () method
a5.reshape(3,8)
a5.max()
a5.min()
a5.mean()
a5.argmax()
a5.argmin()
sum(a5)
a5.sum(axis=0) #column wise sum
a5.sum(axis=1) #row wise sum
np.where(a5==11) #returns the indices where the condition is true