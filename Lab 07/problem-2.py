try:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    if not (num1.isdigit() and num2.isdigit()):
        raise TypeError("Inputs must be numerical.")

    num1 = int(num1)
    num2 = int(num2)

    print("Sum:", num1 + num2)

except TypeError as error:
    print("TypeError:", error)