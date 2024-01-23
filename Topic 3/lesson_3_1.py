count_numbers = int(input('Введите количество цифр для ввода: '))
counter = 1
count_event = 0

while counter <= count_numbers:
    number = int(input(f'Введите число #{counter}: '))
    if number % 2 == 0:
        count_event += 1
    counter += 1

print(f'Количество четных чисел в данном наборе равно {count_event}')

