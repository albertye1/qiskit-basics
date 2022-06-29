import numpy as np

a = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
print(a)
b = np.average(a, axis=0)
print(b)
print(b[0])
