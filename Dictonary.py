#Dictionary
#this is un orderd key value pair
#dict use more memory - key & values
dictanory = {
  'a':[1,2,3,4],
  'b':'hello',
  'c':1
}

print(dictanory)

dictanory2 ={
  123 :[1,2,3,4],
  True:'hello',
  '[100]':100
}

#keys in the dict should be a immutable value , that means it cnnot be chged aftre the dicleration
print(dictanory2)

#when we insert same key with two values , then the second value will over ride the first Value

user ={
  'name' :'pasindu',
  'age' :24,
  'marks' :10
}

#this will print the user details
print(user)

#this print the age of the user, if didnt exists then print 30
print(user.get('age',30))

#this print the job of the user, if didnt exists then print student
print(user.get('job','student'))

print(user)

#this is a nother way of creatig the user
user2 =dict(name='pasindu')

print(user2)

print('name' in user)
print('name' in user.keys())
print( user.items())

user3=user.copy()
user.clear()
print(user)
print(user3)
user.update({'age':30})
print(user)




















