temperature = int(input('Температура в комнате: '))
desired_temperature = int(input('Желаемая температура в комнате: '))
humidity = int(input('Желаемая влажность воздуха: '))

if temperature > desired_temperature and humidity <= 80:
    print('on')
else:
    print('off')
