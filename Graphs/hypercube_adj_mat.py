import numpy as np

def reduced_hyperq_adjmat(r):
	nodes=pow(2,r)
	M=np.zeros((nodes,r),dtype=np.int)
	for i in range(nodes):
		for j in range(r):
			M[i][j]=i^pow(2,j)	#a^b is a XOR b with the binary values of a and b
	return M

#print(reduced_hyperq_adjmat(3))
