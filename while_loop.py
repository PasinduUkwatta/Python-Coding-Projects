i =0
while i<10:
  print(i)
  i+=1
  print('while loop is running' )
  print(" ")

else:
  print('end of the while loop')


number = [1,8,9,1,0,4,5,1,9,7]

for items in number:
  print(items)

i=0
print(' ')
print('while loop started')
while i<len(number):
  print(number[i])
  i+=1


#we can use while loop when we didint kown the no of ieraions
while True:
  respond = input("Say Something :")
  if(respond=="bye"):
    break
