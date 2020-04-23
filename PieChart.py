from matplotlib import pyplot as plt

slices = [5,4,6,7]
subjects = ['science','maths','english','ict']
cols = ['b','r','y','g']

plt.pie(slices,
        labels= subjects,
        colors=cols,
        startangle=90,
        shadow=True,
        autopct='%1.1f%%'
)

plt.title('Subjects Distribution')
plt.show()