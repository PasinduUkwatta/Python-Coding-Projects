from matplotlib import pyplot as plt
#Histogram Drawing
marks =[1,9,9,4,9,8,7,0,1,8,7,5,9,2,8,4,9,4,5,9,1,9,7,4,8,3,2,0,9,7,5,6,3,1,2,7,3,4,9,0,8,4,7,3,7,4,7]

bins=(0,1,2,3,4,5,6,7,8,9)

plt.hist(marks,bins,histtype='bar',rwidth=.5)

plt.title('Students Marks Distribution')
plt.xlabel('Marks')
plt.xlabel('NO of Students')
plt.legend()
plt.show()
