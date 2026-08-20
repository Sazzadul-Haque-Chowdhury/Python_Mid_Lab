import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
even_numbers = arr[arr % 2 == 0]

print("Original Array:", arr)
print("Even Numbers:", even_numbers)