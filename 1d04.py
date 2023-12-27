list = [1, 2, 4, 6, 5, 3, 7, 8, 9, 10]
print(list)

for i in range(0, 10):
    for a in range(i + 1, 9):
        if list[i] < list[a]:
            list[i], list[a] = list[a], list[i]
print(list)