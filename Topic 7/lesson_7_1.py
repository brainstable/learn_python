def read_verse(path_file):
    text = ''
    with open(path_file, encoding='utf-8') as f:
        for n in range(6):
            text += f.readline()

    return text


print(read_verse('../data/verse.txt'))