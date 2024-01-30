def count_repeat_word(file, word):
    lst = []
    count = 0
    with (open(file, encoding='utf-8') as f):
        lst = f.read().replace('.', '').replace(',', '').replace(';', '').replace(':', '').replace('!', '').replace('?', '').split()

    for l in lst:
        if word.lower() == l.lower():
            count += 1

    return count

print(count_repeat_word('../data/pushkin.txt', 'там'))