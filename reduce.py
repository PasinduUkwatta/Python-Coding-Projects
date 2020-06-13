from functools import reduce

my_list = [2, 4, 6, 8]


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, my_list, 10))
print(my_list)
