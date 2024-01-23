list = [7, 6, 2, 8, 5]

print(list)

fist_item = list.pop(0)
last_item = list.pop(-1)

list.append(fist_item)
list.insert(0, last_item)

print(list)