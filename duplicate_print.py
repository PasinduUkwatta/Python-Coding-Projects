#check the d uplicates in the list and print them back
my_list =['a','b','c','d','m','n','m','d','b']

duplicates = []

for item in my_list:
  if my_list.count(item) >1:
    if item not in duplicates:
      duplicates.append(item)

print(duplicates)
  