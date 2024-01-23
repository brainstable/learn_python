list = [5, 10, 15, 20, 25, 50]

for i in list:
    if i == 20:
        index = list.index(i)
        list[index] = 200

print(list)