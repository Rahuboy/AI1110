# ICSE 2018 Grade 12 17(a)
# Rahul Ramachandran (cs21btech11049)

import numpy as np
from scipy import integrate

#parabola
def integrand(x):
    return np.sqrt(8*x)

I = integrate.quad(integrand, 0, 2)

print("Integral value computed by python is",I[0]*2)
print("Integral value manually calculated was",32/3)

