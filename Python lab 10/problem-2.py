import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
value = 3

positions = np.where(arr == value)

print("Array:", arr)
print("Positions of", value, ":", positions)