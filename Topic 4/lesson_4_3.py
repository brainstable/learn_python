list1 = ["Mike", "", "Emma", "Kelly", "", "Brad", "", "", ""]

count_empty = list1.count("")

for i in range(0, count_empty):
    list1.remove("")

print(list1)