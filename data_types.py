#counter the items in the list
from collections import Counter,defaultdict,OrderedDict

li = [1,2,8,9,7,0,2,6,3,9,0,4,7,2,3,0]
li.sort()
print(li)
print(Counter(li))

#In the default dict we need to provide a default value,when the data does not exisit
#first argument of the default dict is iterable data
dictonary = defaultdict(lambda :'does not exist',{'a' :1,
             'b' :2})

print(dictonary['a'])

#In the ordedrd dictanry insertion order is saved
#So when we acces the data we need to think about the index of the data
dict1 =OrderedDict()
dict1['a'] =1
dict1['b'] =2
dict1['c'] =3
dict1['d'] =4

dict2 =OrderedDict()
dict2['a'] =1
dict2['b'] =2
dict2['c'] =3
dict2['d'] =4

print(dict2==dict1)

d1 =OrderedDict()
d1['a'] =1
d1['b'] =2
d1['c'] =3
d1['d'] =4

d2 =OrderedDict()
d2['c'] =3
d2['a'] =1
d2['b'] =2
d2['d'] =4

#this provide false
#beacuse the insertion order is different
print(d1==d2)