
# Write a Python program that takes a user-input text string and generates a dictionary where:
# Keys are the individual words from the input text.
# Values are the lengths of the corresponding words.

dict={}
m = input("Enter the input string ")
mlsr = m.split(" ")
for i in mlsr:
    key=i
    value=len(i)
    dict[key]=value
print(mlsr)
print(dict)