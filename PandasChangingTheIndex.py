import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

df = pd.DataFrame({'day':[1,2,3,4,5],
                   'attencdence':[39,48,68,22,34]})
print(df)

#chnging the index

df.set_index('day',inplace=True)

df.plot
plt.show()

#changing the column header
df = df.rename(columns={"day":"weekdays"})

print(df)

#connecting two data sets into one set
Student1 = pd.DataFrame({'assignment':[1,2,3,4,5],'attencdence':[45,679,3,78,34],'total':[67,94,38,74,89]}, index =[1,2,3,4,5])
Student2 = pd.DataFrame({'Id':[1,2,3,4,5],'rank':[45,679,3,78,34],'degree':['it','it','itm','itm','it']}, index =[6,7,8,9,10])

concat = pd.concat([Student1,Student2])
print(concat)