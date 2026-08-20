import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

row_sum = np.sum(arr, axis=1)

column_sum = np.sum(arr, axis=0)

print("Array:")
print(arr)

print("Sum of each row:", row_sum)
print("Sum of each column:", column_sum)