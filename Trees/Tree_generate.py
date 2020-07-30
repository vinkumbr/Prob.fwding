#To create the reduced adjacency matrix of an m-ary tree

import numpy as np
m = int(input('Enter the d for d-ary tree.'))
height = int(input('Enter the height of the tree. (root is at height 0)'))
nodes = int((m**(height+1)-1)/(m-1))
M = []
q = 1
for i in range(nodes):
	if i<int(nodes/m):
		children = [chil for chil in range(q,q+m)]
		q = q+m
		M.append(children)
	else:
		M.append([int((i-1)/m)])       #leaf nodes

with open('./Tree_%d_%d.txt'%(m,height), 'w') as f:
    for item in M:
        f.write("%s\n" % item)
