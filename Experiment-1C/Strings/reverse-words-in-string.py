'''Reverse Words in a Sentence
Reverses the order of words in a given string while keeping each word intact.  [split() and join()] '''

str = input("Enter a sentence: ")

word = str.split()
rev_word = word[::-1]
rev_str = " ".join(rev_word)
print("Reversed sentence:", rev_str)
