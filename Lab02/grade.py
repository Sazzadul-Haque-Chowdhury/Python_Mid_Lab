marks = int(input("Enter your marks: "))

if marks < 50:
    print("Grade: F")
elif marks <= 59:
    print("Grade: D")
elif marks <= 64:
    print("Grade: D+")
elif marks <= 69:
    print("Grade: C")
elif marks <= 74:
    print("Grade: C+")
elif marks <= 79:
    print("Grade: B")
elif marks <= 84:
    print("Grade: B+")
elif marks <= 89:
    print("Grade: A")
else:
    print("Grade: A+")