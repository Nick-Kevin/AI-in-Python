import numpy as np
from numpy.linalg import eig

a = np.array([[1, 2], [2, 1]])

w,v = eig(a)
print("E-value", w)
print("E-vector", v)
