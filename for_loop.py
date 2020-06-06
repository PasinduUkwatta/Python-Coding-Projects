#loops

for items in 'pasindu thiwanka deshan':
  print(items)


for numbers in [1,2,3,4,5,6,7,8,9,7,8,1,3,0,1,6,8]:
  print(numbers)

#nested for loop
for number in (1,2,3,4,5):
  for letter in ['a','b','c']:
    print(number,letter)


#iterable -list,dictonary,tuple,set,string

#iterated -one by one check each item in the collection

user ={
  'name' :'pasindu',
  'age' :24,
  'marks' :10
}

#we can loop through the object and get the keys of the dictonary
for details in user:
  print(details)

#this will give keys and values as a tuple
for  details in  user.items():
  print(details)

#this will produce the values in the dictonary
for  details in  user.values():
  print(details)

#seperate key and value in the dictonary
for key,value in user.items():
  print(key,value)

#intergers cannotbe iterated