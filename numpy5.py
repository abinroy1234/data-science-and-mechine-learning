import numpy as np

A = np.array([[1,2,3],[2,3,4],[3,4,5]])

u,v,w = np.linalg.svd(A,full_matrices=False)
print("u\n",u)
print("v\n",v)
print("w\n",w)
