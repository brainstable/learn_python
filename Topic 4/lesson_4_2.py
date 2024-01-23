list = [5, 10, 15, 20, 25, 50]

for number in list:
    if number == 20:
        index = list.index(number)
        list[index] = 200

print(list)