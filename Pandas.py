import pandas as pd
#print the data list


Faculty ={'number':[1,2,3,4,5,6],'Rank':[46,8,303,947,4,980],'Degree':['IT','ITM','IT','IT','ITM','ITM']}

df = pd.DataFrame(Faculty)

print(df)

print()
Student = {'id':[2,3,4,5,6,],'subject':['maths','science','it','cse','commersce'],'marks':[20,40,65,70,89]}

list = pd.DataFrame(Student)
print(list)

#slicing

print(df.head(2))
print(list.tail(3))

#merging

Student1 = pd.DataFrame({'Id':[1,2,3,4,5],'rank':[45,679,3,78,34],'marks':[67,94,38,74,89]}, index =[1,2,3,4,5])
Student2 = pd.DataFrame({'Id':[1,2,3,4,5],'rank':[45,679,3,78,34],'marks':[67,94,38,74,89]}, index =[6,7,8,9,10])

merge = pd.merge(Student1,Student2,on='rank')
print(merge)


#joining

Student1 = pd.DataFrame({'assignment':[1,2,3,4,5],'attencdence':[45,679,3,78,34],'total':[67,94,38,74,89]}, index =[1,2,3,4,5])
Student2 = pd.DataFrame({'Id':[1,2,3,4,5],'rank':[45,679,3,78,34],'degree':['it','it','itm','itm','it']}, index =[6,7,8,9,10])

join = Student1.join(Student2)
print(join)

join = Student2.join(Student1)
print(join)






