'''Given two sets: 
A = {1,2,3,4,5} 
B = {4,5,6,7,8} 
 
Find: 
1. A union B 
2. A intersection B 
3. A - B '''
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

union_set = A.union(B)
intersection_set = A.intersection(B)
difference_set = A.difference(B)

print("A union B:", union_set)
print("A intersection B:", intersection_set)
print("A - B:", difference_set)