#debugging
#linting
#IDE/Editor
#Read Errors
#PDB -Python Debug

import pdb

def addTwo(num1, num2):
    pdb.set_trace()
    total = 20+10
    print(num1 + num2)
    return num1+num2 

addTwo(1,2)


#help list - this will produce the source code
#step
#a
#w
#we can  change variables in the pdb