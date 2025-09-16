# #Write a Python program that:
# Asks the user to enter a two-digit integer (between 10 and 99).
# Returns the number in word format using dictionary concepts.
# Handles invalid inputs gracefully.
d1 = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty"
}

d2 = {
    1: "one",
    2: "twenty",
    3: "thirty",
    4: "fourty",
    5: "fivety",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety",

}

f=int(input("enter the number "))
n=str(f)
if(f<=20):
    print(f"{n} = ",d1[f])
elif(f>20):
    print(f"{n} = "+str(d2[int(n[0])])+"-"+str(d1[int(n[1])]))

