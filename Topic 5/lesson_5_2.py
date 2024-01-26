def average(*args):
    sum = 0
    count = 0
    for arg in args:
        sum += arg
        count += 1
    return sum / count

print(average(1, 2, 3, 4, 5))