import numpy as np

def adjmatdoubletree(height):
	size=2**(height+1)-1+(2**height)-1
	a=np.zeros((size,size))
	for i in range(2**(height)-1):
		a[i][2*i+1]=1
		a[i][2*i+2]=1
	j=size-1
	k=1
	while j>=size-((2**height)-1):
		a[j][size-2*k]=1
		a[j][size-2*k-1]=1
		j=j-1
		k=k+1
	a=a+np.matrix.transpose(a)
	return a

def reduce_adj_mat(a):
	M=[[] for i in range(len(a))]
	for i in range(len(a)):
		for r in min(np.where(a[i][:])):
			M[i].append(r)
	return M

#For a doubletree (two binary trees joined at the leaves) of height (root of one of the trees is the source and is at height 0; height is the level at which there are maximum nodes) given by the variable height.
height = input('Enter the height')
a=adjmatdoubletree(height)
M=reduce_adj_mat(a)
with open('./M_doubletree_%d.txt'%(height), 'w') as f:
    for item in M:
        f.write("%s\n" % item)
