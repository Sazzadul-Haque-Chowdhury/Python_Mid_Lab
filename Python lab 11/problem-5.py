import numpy as np

arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([2, 4, 5, 8])

sum1 = np.sum(arr1)
sum2 = np.sum(arr2)

prod1 = np.prod(arr1)
prod2 = np.prod(arr2)

diff1 = np.diff(arr1)
diff2 = np.diff(arr2)

print("Array 1:", arr1)
print("Array 2:", arr2)

print("Sum of Array 1:", sum1)
print("Sum of Array 2:", sum2)

print("Product of Array 1:", prod1)
print("Product of Array 2:", prod2)

print("Difference of Array 1:", diff1)
print("Difference of Array 2:", diff2)