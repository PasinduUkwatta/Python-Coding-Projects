import array as arr

a = arr.array('i',[2,9,8,4,8,0,1,4,7,1,0,7,4])

#variable must declare as a zero at the begining
b=0
print('array while loop')

#always take the length of te array for while looping
while b<len(a):
    print(a[b])

    #incerement the value after one loop
    b=b+1
