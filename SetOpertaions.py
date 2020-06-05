my_set = {1,2,3,4,5,6}

your_set = {2,8,4,1,8,4,6,3,4,8,9,1,3,5,2,8,2}

print(my_set)
print(your_set)


#this method compare first one with the second one and show the difference in the first method
print(my_set.difference(your_set))
print(your_set.difference(my_set))

#discard will remove the selected element from the set
my_set.discard(6)
print(my_set)

print('intersection is '+str(my_set.intersection(your_set)))

#this will give the union of the two sets
print(my_set.union(your_set))


print(my_set.issubset(your_set))
print(your_set.issuperset(my_set))