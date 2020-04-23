import numpy as np
import matplotlib.pyplot as plt
a= np.array([(1,2,3,4,5),(4,5,6,7,8),(6,7,8,9,0)])
print(a)

#data size
print(a.itemsize)
print(a.dtype)

#dimention of the array
print(a.ndim)

#no of elemnts in the array
print(a.size)

#shape of the array
print(a.shape)

c=np.array([(2,3,4,5),(3,4,5,6)])
d=np.array([(9,8,7,4),(6,8,4,9)])

#resgaping the array
print(c.reshape(4,2))
print(d.reshape(8,1))

#slizing an array
print(c[0,3])
print(d[1,2])
print(c[0:,2])

a=np.linspace(2,4,9)
print(a)

#min and max of the array
print(c.max())
print(d.min())

#sum of the array
print(c.sum())
print(d.sum())

#axis sum
print(a.sum(axis=0))
print(c.sum(axis=0))

#sureroot and standred devisation
print(np.sqrt(c))
print(np.std(d))

#sum of the two arrays
print(c+d)

#print all values in single column
print(c.ravel())

#graph drwaing
x= np.arange(0,3*np.pi,0.1)

y= np.sin(x)

plt.plot(x,y)

plt.show()


ar = np.array([3,4,5,6])

print(np.log10(ar))