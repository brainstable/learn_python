list1 = ["Mike", "", "Emma", "Kelly", "", "Brad", "", "", ""]

no_empty = list(filter(lambda x: x, list1))

print(no_empty)