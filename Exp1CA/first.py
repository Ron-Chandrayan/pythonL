# Reverse Words in a Sentence
# Reverses the order of words in a given string while keeping each word intact. [split]

str1 = input("enter the sentence ")
lstr=str1.split(" ")
# print(lstr)
rstr=lstr[::-1]
rstr = " ".join(rstr)
print(rstr)