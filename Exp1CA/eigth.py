# String Compression aaabbc → a3b2c1
# Compresses consecutive repeated characters (e.g., "aaabbc" → "a3b2c1").

str1 = input("Enter the string: ")

if not str1:
    print("Empty string")
else:
    compressed = ""
    i = 0
    
    while i < len(str1):
        current_char = str1[i]
        count = 1
        
        # Count consecutive occurrences of the same character
        while i + 1 < len(str1) and str1[i] == str1[i + 1]:
            count += 1
            i += 1
        
        # Add character and its count to the result
        compressed += current_char + str(count)
        i += 1
    
    print(f"Original string: {str1}")
    print(f"Compressed string: {compressed}")
