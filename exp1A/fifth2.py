# #Check and print whether num is a BUZZ Number or not.
# A number is said to be a BUZZ number if it is exactly divisible by 7 or ends with 7].
# Example 1: IN=27, then 27 is a BUZZ number (because it ends with 7).
# Example 2: If N=49, then 49 is a BUZZ number (because it is divisible by 7).
# Example 3: If N=15, then 15 is NOT a BUZZ number.
# For an incorrect option, an appropriate error message should be displayed.

num = input("enter the number to check ")
if((int(num)%7==0) or (num[-1]=="7")):
    print("buzz number")
else:
    print("not buzz number")
