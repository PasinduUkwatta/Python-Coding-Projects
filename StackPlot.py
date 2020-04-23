from matplotlib import pyplot as plt
#stackplot drwaing
days =[1,2,3,4,5]

sleeping =[7,8,3,4,3]
eating=[2,8,4,6,3]
working=[2,5,7,8,3]
playing=[6,8,4,3,2]

#define this to identife the gaps between lines
plt.plot([],[],color='b',label ='sleeping',linewidth =5)
plt.plot([],[],color='r',label ='eating',linewidth =5)
plt.plot([],[],color='g',label ='working',linewidth =5)
plt.plot([],[],color='y',label ='playing',linewidth =5)

plt.stackplot(days,sleeping,eating,working,playing,colors=['b','r','g','y'])

plt.title('Day of My Life')
plt.xlabel('hours')
plt.ylabel('time')
plt.legend()

plt.show()