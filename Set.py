#Sets

#unorderd set of unique set
#no duplicates
my_set = {1,2,4,4,4,3,4,5,6,6,6,4,4,3}
my_set.add(100)
my_set.add(101)
my_set.add(4)

print(my_set)

my_list = [1,2,3,4,5,6,3,4,2,2,3,2,4,3]
print(type(my_list))

# we can wrap the list with the set function
#then the duplicates will be removed
my_set2 =set(my_list)
print(type(my_set2))
print(my_set2)

#check the availabulity
print(4 in my_set)