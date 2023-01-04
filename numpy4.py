import numpy as np

A = np.array([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]])

print("Initial Matrix \n",A)

print("a \n", A[1:4])
print("b\n", A[:, 0:3])
print("c\n", A[1:3, 0:2])
print("d\n", A[:, 1:3])
print("e\n", A[0:1, 1:3])
