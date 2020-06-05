#tuple
#tuple is immutable
#tuple is good in performance
my_tuple = (1,2,3,4,5,6,7)

print(my_tuple)
print(my_tuple[4])


my_tuple =(1,2,3,4,5,6,7)

#tuple slicing
new_tuple = my_tuple[1:4]

print(new_tuple)


a,b,c,d,e,f,*others =(12,3,4,56,7,78,9,3,4,8,2,9,42)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(others)

numbers = (2,904,5,71,7,58,10,40)

#this will give the no of appernces in the given value
print(numbers.count(5))

print(numbers.index(58))

print(len(numbers))

#reverse the tuple
print(numbers[::-1])