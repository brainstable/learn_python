import requests


def get_status_and_url(url):
    r = requests.get(url)
    return r.status_code, r.url


print(get_status_and_url('https://www.google.ru'))
