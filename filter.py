# filter will create a new list without affecting the given list

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def only_odd(items):
    return items % 2 == 1


print(list(filter(only_odd, list_1)))

print(list_1)
