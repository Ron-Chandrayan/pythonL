# Format Phone Number 1234567890 → (123) 456-7890
# Converts a string of 10 digits into the format (XXX) XXX-XXXX

str=input("enter phone number ")
tstr=str[:3:]
print(tstr)
lstr=str[4:7:]
print(lstr)
fstr="("+tstr+") "+lstr+"-"+str[7::]
print(fstr)

