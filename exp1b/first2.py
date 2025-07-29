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

for i in range(1, row + 1):
    if i % 2 == 0:
        # Even row: print even numbers
        for k in range(2, (i * 2) + 1, 2):
            print(k, end=" ")
    else:
        # Odd row: print odd numbers
        for k in range(1, (i * 2), 2):
            print(k, end=" ")
    print("\n")
