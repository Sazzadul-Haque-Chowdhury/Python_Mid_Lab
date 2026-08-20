import numpy as np

arr = np.array([1, 3, 5, 6, 7, 8, 9, 11])
K = 3

smallest_values = np.sort(arr)[:K]

print("Array:", arr)
print("The", K, "smallest values:", smallest_values)