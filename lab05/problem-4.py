def search(lst, key):
    for i in range(len(lst)):
        if lst[i] == key:
            return i
    return -1

numbers = [10, 20, 30, 40, 50, 60]
print(numbers)
key = int(input("Enter the value to search: "))

result = search(numbers, key)

if result != -1:
    print("Value found at index", result)
else:
    print("Value not found")