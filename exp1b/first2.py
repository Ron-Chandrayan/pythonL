# 54321
# 4321
# 321
# 21
# 1
# row = 5
# for i in range(row,0,-1):
#     for k in range(i,0,-1):
#         print(k, end=" ")
#     print("\n")

row = 5
c=1
for i in range(1,row+1):
    if(i%2==0):
        for k in range(2,(i*2)+1,2):
            print(k, end=" ")
    else:
        for k in range(1,i+c,2):
            print(k, end=" ")
            c=c+2
    print("\n")