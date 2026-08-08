numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter the index: "))
    print("Element:", numbers[index])

except IndexError:
    print("Error: Index is out of range.")

except TypeError:
    print("Error: Index must be an integer.")