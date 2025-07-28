#Write a program to input a character in ch. Convert ch into lowercase letter if it is in uppercase otherwise convert into uppercase if it is in lowercase. Print the original and new character.

ch = input("enter the character ")
if(ch.isupper()):
    print("the character is ",(ch.lower()))
else:
     print("the character is ",(ch.upper()))