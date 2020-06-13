my_list =[2,3,4,5,6]
def multiply_by_2(item):
    return item*2

#in this function my_list didnt affect
#this create a new list
#my_list stays same as the start
print(list(map(multiply_by_2,my_list)))

print(my_list)