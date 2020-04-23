from matplotlib import pyplot as plt

x=([1,2,3,4,5,7,1,4,3,7,3,4,2])
y=([0,3,9,7,3,6,4,5,2,4,3,5,3])

plt.scatter(x,y,label ='skiscat' ,color='k')
plt.xlabel('No of Students')
plt.ylabel('Marks')
plt.title('Scatter Diagram of Students Marks')
plt.legend()

plt.show()


