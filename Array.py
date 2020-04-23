import array as arr

a= arr.array('i',[1,2,3,4,5,7,9,8,0,5,0])
b= arr.array('i',[7,6,9,9,3,0,1,1,4,4,1,3,4,3])
c= arr.array('i')
c= a+b
print(c)
print(a[3:7])
print(c[4:9])
print(b[2:5])

print(a)

print(a[2])
print(a[-2])
print(len(a))


print(a)
a.extend([45,67,43])
print(a)
a.insert(4,0)
print(a)


print(a.pop())
print(a.pop(2))
a.remove(5)

print(a)