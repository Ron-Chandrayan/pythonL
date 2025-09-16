
# Replace Words with Synonyms
# Replaces words in a string using a provided synonym dictionary.

syn={"good":"fine","bad":"not good","goodbye":"pranipat"}
str=input("Enter string ")
lstr=str.split()
print(lstr)
for i in range(0,len(lstr),):
    for key,value in syn.items():
        if(key==lstr[i]):
            lstr[i]=value
fstr=" ".join(lstr)
print(fstr)