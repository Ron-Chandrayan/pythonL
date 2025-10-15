import numpy as np

def main():
    print("===== NumPy Interactive Demo =====")
    
    # 1️⃣ Create Arrays
    print("\n1. Creating Arrays")
    arr1 = np.array([10, 20, 30, 40, 50])
    arr2 = np.arange(1, 11)       # 1 to 10
    arr3 = np.linspace(0, 1, 5)   # 5 numbers between 0 and 1
    arr4 = np.ones((2,3))
    arr5 = np.zeros((3,2))
    arr6 = np.eye(3)
    
    print("arr1:", arr1)
    print("arr2:", arr2)
    print("arr3:", arr3)
    print("arr4 (ones 2x3):\n", arr4)
    print("arr5 (zeros 3x2):\n", arr5)
    print("arr6 (identity 3x3):\n", arr6)
    
    # 2️⃣ Array Attributes
    print("\n2. Array Attributes")
    print("Shape of arr2:", arr2.shape)
    print("Number of dimensions of arr4:", arr4.ndim)
    print("Item size of arr1:", arr1.itemsize, "bytes")
    
    # 3️⃣ Math Operations
    print("\n3. Math Operations on arr1")
    print("Original arr1:", arr1)
    print("Add 5:", arr1 + 5)
    print("Multiply by 2:", arr1 * 2)
    print("Sin values:", np.sin(arr1))
    print("Sum:", np.sum(arr1))
    print("Mean:", np.mean(arr1))
    
    # 4️⃣ Indexing & Slicing
    print("\n4. Indexing & Slicing arr2")
    print("arr2:", arr2)
    print("arr2[2:7]:", arr2[2:7])
    print("arr2[::2] (every 2nd element):", arr2[::2])
    print("arr2[-3:] (last 3 elements):", arr2[-3:])
    
    # 5️⃣ Reshaping
    print("\n5. Reshaping arr2 to 2x5")
    arr2_reshaped = arr2.reshape(2,5)
    print(arr2_reshaped)
    
    # 6️⃣ Multidimensional Arrays
    print("\n6. Multidimensional Array Operations")
    arr_multi = np.array([[1,2,3],[4,5,6],[7,8,9]])
    print("Original 3x3 array:\n", arr_multi)
    print("All rows, all columns:\n", arr_multi[:,:])
    print("First two rows, last two columns:\n", arr_multi[:2,1:])
    print("Transpose:\n", arr_multi.T)
    
    # Optional interactive selection
    while True:
        choice = input("\nEnter 1 for sum, 2 for mean, 3 for max, 4 for min, 0 to exit: ")
        if choice == '1':
            print("Sum of arr1:", np.sum(arr1))
        elif choice == '2':
            print("Mean of arr1:", np.mean(arr1))
        elif choice == '3':
            print("Max of arr1:", np.max(arr1))
        elif choice == '4':
            print("Min of arr1:", np.min(arr1))
        elif choice == '0':
            print("Exiting interactive demo.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
