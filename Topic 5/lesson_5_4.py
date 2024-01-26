list1 = ["Mike", "", "Emma", "Kelly", "", "Brad", "", "", ""]

x = lambda lst: list(filter(None, lst))

print(x(list1))