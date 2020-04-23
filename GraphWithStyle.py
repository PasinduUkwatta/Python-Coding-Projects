from matplotlib import pyplot as plt
from matplotlib import style

#using the graph style
style.use('ggplot')

x1=[1,2,3,4,5,6]
y1=[2,4,6,4,8,4]


x2=[1,2,3,4,5,6]
y2=[8,6,2,9,4,7]


plt.title('Attendence Report')
plt.xlabel('NO of Students')
plt.ylabel('Classrooms')

#giving line name and width
plt.plot(x1,y1,'g',label = 'first month',linewidth=4)
plt.plot(x2,y2,'c',label = 'second month',linewidth=4)

#showing the line name at the coner of the graph
plt.legend()

#gris colour is black
plt.grid(True,color ='k')

plt.show()