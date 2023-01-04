import numpy as np

A = np.matrix([[2, 1, -2], [3, 0, 1], [1, 1, -1]])

B = np.matrix([-3,5,-2])
y = np.linalg.inv(A)

X = np.matmul(B, y)

print("X\n{}\n".format(X))
