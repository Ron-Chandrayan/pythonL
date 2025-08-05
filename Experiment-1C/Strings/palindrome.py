'''Check Palindrome  A man a plan a canal Panama → True   

Check string is a palindrome (ignoring spaces and case) or not. '''

sentence = input("Enter a string: ")

st = sentence.replace(" ", "").lower()

if st == st[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")