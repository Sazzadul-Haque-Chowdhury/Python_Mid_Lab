def palindrome(text):
    if text == text[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")

word = input("Enter a string: ")
palindrome(word)