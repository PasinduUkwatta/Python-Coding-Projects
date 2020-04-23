import array as arr

a  = arr.array('i',[1,2,3,6,7,8,9,4])

print(a)
print('all values')
for x in a:
    print(x)

b = arr.array('i',[9,2,8,3,7,9,4,9,0,5,70,2,0])

print(b)
print('all values in b :')
for y in b:
    print(y)
print('all values in b :')
for y in b[0:7]:
    print(y)