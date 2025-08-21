#Keys are the integers from the input list.
# Values are the strings "even" or "odd", indicating the parity of each integer.
import math
dict={}
while(True):
    m=int(int(input("enter positive number ")))
    s=bin(abs(m))
    key=abs(m)
    p=s.count('1')
    if(p%2==0):
        value="even"
    else:
        value="odd"
    dict[key]=value
    c=int(input("press 1 to continue 2 to break "))
    if(c==1):
        pass
    else:
        break

print(dict)
