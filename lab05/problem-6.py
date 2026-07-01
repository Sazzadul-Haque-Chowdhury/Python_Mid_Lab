numbers = [10, 20, 30, 20, 50, 50, 60, 20]

new_list = []

for i in numbers:
    if i not in new_list:
        new_list.append(i)

print("Actual list:                   ",numbers)
print("List after removing duplicates:", new_list)