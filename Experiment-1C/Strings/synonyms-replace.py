#Replace Words with Synonyms. Replaces words in a string using a provided synonym dictionary. 
synonyms = {'happy':'joy', 'sad':'upset', 'quick': 'fast'}

str = input("Enter a string: ")
words = str.split()
print(words)

for i in range(len(words)): 
  if words[i] in synonyms:
    words[i] = synonyms[words[i]]
print(words)
new_str = " ".join(words)
print(new_str)