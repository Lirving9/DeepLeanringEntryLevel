import numpy as np
x = np.array([0, 1])
w = np.array([0.5, 0.5])
b = -0.7

ca1 = w*x
ca2 = np.sum(w*x)
ca3 = np.sum(w*x) + b

print(ca1, ca2, ca3)
