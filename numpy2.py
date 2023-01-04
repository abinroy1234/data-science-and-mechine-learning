import numpy as np

ar = np.random.randint(10, size=(3, 3))
print("The initial matrix \n",ar)
print("Inverse \n", np.linalg.inv(ar))
print("Rank \n", np.linalg.matrix_rank(ar))
print("Determinant \n", np.linalg.det(ar))
print("Transform to 1D array\n", ar.flatten())
u, v = np.linalg.eig(ar)
print("Eigen values \n", u)
print("Eigen vectors \n", v)
