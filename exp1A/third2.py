#The telephone department wishes to compute monthly telephone bills for its customers using the following slabs on the basis of calls made:
# Number of calls Rate
# First 200 calls 1.00 per call
# Next 200 calls 30.80 per call
# Next 200 calls 0.50 per call
# Any call above 600 calls 30.40 per call
# Write a program to input number of calls and compute total bill amount. Print the output including the number of calls consumed and the bill amount to be paid.

call = int(input("enter the number of calls "))
if(call<=200):
    bill = 200
elif(call>200 or call<=400):
    bill = 200 + ((call-200)*30.8)
elif(call>400 or call<=600):
    bill = 200 + ((call-200)*30.8) + ((call-400)*0.50)
elif(call>600):
    bill= 200 + ((call-200)*30.8) + ((call-400)*0.50) + ((call-600)*30.40)
print("the total bill is ",bill)