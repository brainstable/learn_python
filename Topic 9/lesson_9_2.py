def get_url_with_parameters(url, parameters):
    split_url = url.split('?')
    split_parameters = split_url[1].split('&')

    if len(parameters) == 0:
        return split_url[0]

    temp_parameters = []

    i = 0
    while i < len(split_parameters) and i < len(parameters):
        temp_parameters.append((split_parameters[i]).replace('@', parameters[i]))
        i += 1

    return str(split_url[0] + '?' + '&'.join(temp_parameters))


url = 'https://www.ozon.ru/search/?from_global=@&sorting=@&text=@'
parameters = ['true', 'price', 'd3']

print(get_url_with_parameters(url, parameters))