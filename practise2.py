friends = {'bob', 'rolf', 'smith'}
abroad = {"bob", "smith"}

local_friends = friends.difference(abroad)

print(local_friends)

art = {'bob', 'smith', 'roy'}
science = {'bob', 'john', 'smith'}

union_friends = art.union(science)

print(union_friends)

my_list = [10, 40, 50]

my_tupple = (25,)
print(type(my_tupple))

set1 = {5, 77, 9, 22, 99, 10}
set2 = {5, 77, 9, 22}

print(set1.intersection(set2))

print(5 == 5)

print(friends == abroad)
print(friends is abroad)

day_of_the_week = input('What is the day of the week ?').lower()
day = (day_of_the_week == "monday")

print(day)


