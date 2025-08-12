# Counts of vowels and consonants in the string.

str = input("enter the email ")
lstr=str.split("@")
print(lstr[0])
nstr=""
for i in range((len(lstr[0]))):
  if(i>=2 and i<=(len(lstr[0])-3)):
    nstr = nstr+"*"
  else:
    nstr=nstr+lstr[0][i]
print(nstr+"@"+lstr[1])