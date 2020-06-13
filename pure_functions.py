# funtion to multiply given list by two
# Rule 1 - Always produce the same result at any time
# Rule 2 -This should not effect to the out side world
def multiply_by_2(li):
    new_list = []
    for items in li:
        new_list.append(items * 2)
    return new_list


print(multiply_by_2([1, 2, 3, 4, 5]))


def multiply_by_5(li):
    new_list = []
    for items in li:
        new_list.append(items * 5)
    return new_list


print(multiply_by_5([3, 4, 5, 6]))
