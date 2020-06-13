my_list = [3, 4, 5, 6, 7]

# this will print the squre values of the given list
# [9, 16, 25, 36, 49]
print(list(map(lambda item: item ** 2, my_list)))

my_list_2 = [(0, 2), (4, 3), (9, 9), (10, -1)]

# this will print the list sorted according to the key in the index
# [(10, -1), (0, 2), (4, 3), (9, 9)]
my_list_2.sort(key=lambda item: item[1])

print(my_list_2)


