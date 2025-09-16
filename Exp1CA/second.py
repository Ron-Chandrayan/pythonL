# Check Palindrome A man a plan a canal Panama → True
# Check string is a palindrome (ignoring spaces and case) or not.

str1=input("Enter the string ")
temp=str1
# print(str1.strip())
str1=str1.replace(" ","")
# print(str1)
str1=str1.lower()
# print(str1)
rstr1=str1[::-1]
# print(rstr1)
if(str1==rstr1):
  print("palindrome")
else:
  print("not palindrome")