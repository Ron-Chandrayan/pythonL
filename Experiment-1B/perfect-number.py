def factors(n):
    l = []
    for i in range(1, n):
     if n % i == 0:
        l.append(i)
    return l

def is_perfect(num):
    l = factors(num)
    if sum(l) == num:
        return True 
    else:
        return False
n = int(input("Enter the upper limit n: "))

print(f"Perfect numbers from 1 to {n} are:")
for i in range(1, n + 1):
    if is_perfect(i):
        print(i)