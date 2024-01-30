def read_last(file):
    lst = []
    words = []
    length_max = 0
    with open(file, encoding='utf-8') as f:
        lst = f.read().split()

    for l in lst:
        word = delete_punctuation(l)
        length_word = len(word)
        if length_word >= length_max:
            length_max = length_word
            words.append(word)
            for w in words:
                if len(w) < length_max:
                    words.remove(w)

    return words

def delete_punctuation(word):
    return word.replace('.', '').replace(',', '').replace(';', '').replace(':', '').replace('!', '').replace('?', '')

print(read_last('../data/pushkin.txt'))