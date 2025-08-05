# Count Vowels and Consonants
def check(str1):

  vowel = 0
  consonant = 0
  space = 0
  size = len(str1)

  for i in range(0, size):
     ch = str1[i]
     ch = ch.lower()

     if (ch == 'a' or ch == 'e' or ch == 'i'
                        or ch == 'o' or ch == 'u'):
       vowel += 1

     elif(ch == " "):
      pass

     else:
      consonant += 1
  print("Vowels:", vowel)
  print("Consonant:", consonant)

str1 = input("Enter a string: ")
check(str1)