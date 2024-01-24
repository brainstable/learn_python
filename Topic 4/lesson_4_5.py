lst1 = ['Санкт-Петербург', 'Москва', 'Казань']
lst2= ['Воронеж', 'Санкт-Петербург', 'Иваново']

set1 = set(lst1)
set2 = set(lst2)

list1 = list(set1.intersection(set2))
print(list1)

list2 = list(set1.symmetric_difference(set2))
print(list2)