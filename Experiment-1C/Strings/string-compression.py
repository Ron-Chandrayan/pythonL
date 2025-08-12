#25. String Compression  aaabbc → a3b2c1. Compresses consecutive repeated characters (e.g., "aaabbc" → "a3b2c1"). 

statement = input()
list_count = []
count = 1

for i in range(1, len(statement)):
    if statement[i] == statement[i-1]:
        count += 1
    else:
        list_count.append(statement[i-1] + str(count))
        count = 1
list_count.append(statement[-1] + str(count))
print(list_count)
print(" ".join(list_count))

