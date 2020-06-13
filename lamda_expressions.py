# one time anounymoues functions
from functools import reduce
# lambda param:action(param)
my_list = [1, 2, 3, 4, 5]
my_list_2=[2,4,6,8,10]


print(list(map(lambda item: item * 2, my_list)))

print(list(filter(lambda items:items%2==1,my_list)))

print(reduce(lambda acc,item:acc+item,my_list))

