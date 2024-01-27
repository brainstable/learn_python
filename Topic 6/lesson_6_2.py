class ListWorker:

    def __init__(self, *args):
        self.list = []
        for arg in args:
            self.list.append(arg)

    def get_numbers(self):
        return list(filter(lambda x: type(x) == int, self.list))

    def get_strings(self):
        return list(filter(lambda x: type(x) == str, self.list))

    def get_others(self):
        return list(filter(lambda x: type(x) != int and type(x) != str, self.list))


lw = ListWorker(1, 5, 'car', 8, [1, 2, 3], 'road', 'tree', 5, (10, 20))

print(lw.get_numbers())
print(lw.get_strings())
print(lw.get_others())