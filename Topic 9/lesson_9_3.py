import requests
from urllib.parse import quote

def count_languages_on_github(languages):
    repositories = []

    for language in languages:
        encoded_languages = quote(language)
        url = f'https://api.github.com/search/repositories?q=language:{encoded_languages}&order=desc&per_page=1&page=1'
        r = requests.get(url)
        if r.status_code == 200:
            repositories.append([language, r.json()['total_count']])
        else:
            repositories.append([language, f'error: {r.status_code}'])

    return repositories

languages = ['python', 'c++', 'java', 'javascript', 'ruby', 'c#']
print(count_languages_on_github(languages))