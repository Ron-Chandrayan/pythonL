#Input points scored by a player and using ternary operators, store "W (winner) in a variable result, if score is greater than or equal to 5 otherwise store 'R' (runner) in a variable result

score = int(input("Enter points scored"))
result = "W" if(score>=5) else "L"
print(result)