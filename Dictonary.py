myDict = {1:'java',
          2:'c',
          3:'python',
          }

print(myDict)
print(type(myDict))

myDict[1] ='html'
myDict[4]='javascript'
print(myDict)

myDict.pop(1)
print(myDict)
myDict.__delitem__(3)
#myDict.clear(2)
print(myDict)
newDict = dict(JAVA=1)
print(newDict)
print(type(myDict))

print(myDict)
print(myDict.keys())
print(myDict.items())
print(myDict.values())
print(myDict.get(1))
print(myDict.get(2))
print(myDict.get(3))

print('normal for loop')
for x in myDict:
    print(x)

print('full detail loop')
for x in myDict.items():
    print(x)

print('values only looping')
for x in myDict.values():
    print(x)

import pandas as pd

c = pd.DataFrame(myDict)
print(pd)
