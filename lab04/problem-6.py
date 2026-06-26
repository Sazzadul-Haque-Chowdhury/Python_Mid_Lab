check = lambda string, sub: string.startswith(sub)

string = input("Enter a string: ")
sub = input("Enter a sub-string: ")

if check(string, sub):
    print("correct sub-string")
else:
    print("incorrect sub-string")