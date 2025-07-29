def multiples(n, limit):
    l = []
    for i in range(1, limit //n+1):
            l.append(i*n)
    return l
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
limit = num1 + num2 #LCM cannot be greater than this

l1 = multiples(num1, limit)
l2 = multiples(num2, limit)

print(f"Multiples of {num1} up to {limit}: {l1}")
print(f"Multiples of {num2} up to {limit}: {l2}")

common_multiples = []
for i in l1:
    if i in l2:
        common_multiples.append(i)
print(f"LCM of {num1} and {num2}: {common_multiples}")