def read_last(lines, file):
    lst = []
    with open(file, encoding='utf-8') as f:
        lst = f.readlines()
    lst.reverse()
    return lst[0:lines]


print(read_last(5, '../data/verse.txt'))