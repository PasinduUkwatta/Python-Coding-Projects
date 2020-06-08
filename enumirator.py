#enumerate the objects will poduce the key and the value
#this will produce the index counter

for key,value in enumerate("pasindu thiwanka"):
  print(key,value)


for key,value in enumerate(list(range(100))):
  if (value==50):
    print(f'The index of the {value} is : {key}')
