from scipy import cluster
import scipy
#help(cluster)

#scipy.info(cluster)

#help()

#special functions

from scipy import special

a=special.exp10(4)

print(a)

#getting the sin value
c=special.sindg(45)

print(c)

#intergrations

from scipy import integrate

i = scipy.integrate.quad(lambda x:x*2 + 4,2,6)
print(i)


#fourirer tranformations

from scipy.fftpack import fft,ifft
import numpy as np

x = np.array([1,2,3,4,5])

#fourier tarnform
y = fft(x)
print(y)

#inverse fourier tranform
z=ifft(x)

print(z)

#liner algebra / finfind the inverse matrix
from scipy import linalg
a = np.array([(1,2),(4,5)])
b= linalg.inv(a)
print(b)

#interpolation functions

#from scipy import interpolate

