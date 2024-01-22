a = int(input('Сторона a: '))
b = int(input('Сторона b: '))
c = int(input('Сторона c: '))

if (a + b > c) and (a + c > b) and (b + c > a):
    print('Треугольник существует')
else:
    print('Треуголник не существует')