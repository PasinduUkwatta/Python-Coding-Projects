from matplotlib import pyplot as plt
from matplotlib import  style

style.use('ggplot')

plt.bar([1,3,5,7,9],[6,7,8,9,10], label ='subject 1')
plt.bar([2,4,6,8,10],[9,8,2,3,7], label ="subject 2",color ='g')

plt.legend()
plt.xlabel('No of Students')
plt.ylabel('No of Marks')
plt.title('Students Marks Table')
plt.show()










