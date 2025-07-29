''' b.
1
24
135
2468
13579
'''
n = int(input("Enter range of n: "))
for i in range(1, n):
  if i % 2 != 0:
    for j in range(1, i + 1):
       print(2 * j - 1, end="")
  else:
    for j in range(1, i + 1):
      print(2 * j, end="")

  print()