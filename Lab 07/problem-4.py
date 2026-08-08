import os

file_path = "../Lab 07/sample.txt"

try:
    with open(file_path, "x") as file:
        file.write("This is the first line.\n")

    print("File created successfully.")

    with open(file_path, "w") as file:
        file.write("This content is written using write mode.\n")

    print("Content written successfully.")

    with open(file_path, "a") as file:
        file.write("This line is added using append mode.\n")

    print("Content appended successfully.")

    with open(file_path, "r") as file:
        content = file.read()

    print("\nFile content:")
    print(content)

except FileExistsError:
    print("Error: The file already exists.")

except FileNotFoundError:
    print("Error: The specified directory does not exist.")

except PermissionError:
    print("Error: Permission denied.")

except Exception as error:
    print("Unexpected error:", error)