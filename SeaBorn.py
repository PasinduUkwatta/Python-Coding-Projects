import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#https://github.com/mwaskom/seaborn-data/blob/master/flights.csv
a= sns.load_dataset("flights")
sns.relplot(x='passengers',y='month',data=a)

print(a)

a= sns.load_dataset("flights")
sns.relplot(x='passengers',y='month',hue='year',data=a)
print(a)


a= sns.load_dataset("flights")
b=sns.PairGrid(a)
b.map(plt.scatter)



