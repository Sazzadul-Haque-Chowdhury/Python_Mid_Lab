d = {
    'V': 10,
    'VI': 10,
    'VII': 40,
    'VIII': 20,
    'IX': 70,
    'X': 80,
    'XI': 40,
    'XII': 20
}
frequency = {}
for value in d.values():
    if value in frequency:
        frequency[value] += 1
    else:
        frequency[value] = 1
print(frequency) 