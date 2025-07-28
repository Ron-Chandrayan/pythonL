#Write a Python program to print all numbers from 1 to 10 except numbers divisible by 3. Use a for loop and ensure you use the continue statement to skip numbers divisible by 3.
for i in range(1,11):
    if(i%3==0):
        continue
    else:
        print(i,end=" ")