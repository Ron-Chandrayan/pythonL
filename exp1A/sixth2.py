#Enter two alphabets in cl and c2. Check and display the values of C1 and C2 along with the largest alphabet. if C1 'M' and C2= 'E' then output will be: =Largest alphabet = M. Use Ternary Operator

c1 = input("Enter first character ")
c2 = input("enter second character ")
ans = f"{c1} is greater" if(max(c1,c2)==c1) else f"{c2} is greater"
print(ans)