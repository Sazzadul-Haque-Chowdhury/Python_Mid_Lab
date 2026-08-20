import numpy as np

arr = np.array([1, -2, 3, -4, 5, -6, 7, -8])

arr[arr < 0] = 0

print("Array after replacing negative values:")
print(arr)