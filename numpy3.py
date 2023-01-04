import numpy as np

A = np.array([[1, 2], [3, 4]])
print("(1)")
print(np.multiply(A, np.multiply(A, A)))
print(A * A * A)
print(np.power(A, 3))
print(A ** 3)

print("(2)")
print(np.identity(2, dtype=int))

print("(3)")
print(np.power(A, [[1, 2], [3, 4]]))

print("(4)")
B = np.array([[2, 1], [4, 3]])
print("X^2 + 2Y \n", (A ** 2) + (2 * B))
