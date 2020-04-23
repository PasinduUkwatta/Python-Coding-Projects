import numpy as np
import time
import sys

import scipy as sp
a = np.array([(1,2,3,4,5),(3,4,5,6,7)])
b = np.array([1,2,3,4,5])

print(a)
print(b)
print(a+b)

print(a.size)
S = range(1000)
print(sys.getsizeof(5)*len(S))

D = np.arange(1000)

print(D.size*D.itemsize)


