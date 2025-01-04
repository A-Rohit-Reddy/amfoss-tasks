s = input()
dict1 = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}

for i in s:
    if i in dict1:
        dict1[i] += 1

for i in dict1:
    print(dict1[i], end=" ")
