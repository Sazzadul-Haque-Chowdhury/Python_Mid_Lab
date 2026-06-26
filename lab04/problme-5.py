def count_elements(lst):
    counted = []

    for item in lst:
        if item not in counted:
            count = 0

            for x in lst:
                if x == item:
                    count += 1

            print(item, "=>", count)
            counted.append(item)

# Sample List
numbers = [10, 20, 30, 30, 30, 30, 20, 40]

count_elements(numbers)