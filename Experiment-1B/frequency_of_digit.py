def count_digits(n):
    d = {}
    while n > 0:
        digit = n % 10
        for i in range(0,10):
          if(digit == i):
            if digit in d:
                d[digit] += 1
            else:
                d[digit] = 1
        n //= 10
    print(d)  
n = int(input("Enter a number: "))
count_digits(n)

    