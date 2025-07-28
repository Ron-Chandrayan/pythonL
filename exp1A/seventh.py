#Accept three integer numbers m, n and q. Using suitable mathematical methods find and print the largest number from m, n and q and smallest number from n and q.

m=int(input("enter first integer "))
n=int(input("enter second integer "))
q=int(input("enter third integer "))
maxi = max(m,n,q)
mini = min(m,n,q)
print("Maximum of the number is ",maxi)
print("Minimum of the number is ",mini)
