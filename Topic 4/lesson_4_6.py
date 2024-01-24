my_list = []

while True:
    enter = input('Введите строку или нажмите для выхода q: ')
    if enter == 'q':
        break
    else:
        my_list.append(enter)

print(my_list)