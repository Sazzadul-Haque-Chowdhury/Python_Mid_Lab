list = ['aca', 'xyz', 'aba', '1221', '565']
count = 0
for i in list:
    if len(i) >= 2 and i[0] == i[-1]:
        count += 1

print("Count:", count)