#reference: http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.67.7957&rep=rep1&type=pdf
from __future__ import division

import numpy as np
import random
import scipy.io

def isconnected(M):
	nodes=len(M)
	# Make a copy of the set, so we can modify it.
	number = nodes
	nodes = set(range(1,nodes))
	# Iterate while we still have nodes to process.
	group = {0}
	source = {0}
	# Build a queue with this node in it.
	queue = [0]
	# Iterate the queue.
	# When it's empty, we finished visiting a group of connected nodes.
	while queue:
		# Consume the next item from the queue.
		n = queue.pop(0)
		# Fetch the neighbors.
		neighbors=[]
		for i in M[n]:
			neighbors.append(i)
		# converting it to a set
		neighbors=set(neighbors)
		# Remove the neighbors we already visited.
		neighbors.difference_update(group)
		# Remove the remaining nodes from the global set.
		nodes.difference_update(neighbors)
		# Add them to the group of connected nodes.
		group.update(neighbors)
		# Add them to the queue, so we visit them in the next iterations.
		queue.extend(neighbors)
		#print(queue)
	if not nodes:
		return True
	else:
		return False

def RRG_generate(n,d):
	#check parameters
	if n*d % 2==1:   
		print('createRandRegGraph input err: n*d must be even!')
	stubs = list(range(n))*d
	M=[[] for i in range(n)]
	edgesTested = 0
	repetitions = 1
	while stubs!=[] and repetitions < 20:
		edgesTested = edgesTested+1
		i1 = np.random.choice(range(len(stubs)))
		i2 = np.random.choice(range(len(stubs)))
		v1 = stubs[i1]
		v2 = stubs[i2]

		#check that there are no loops nor parallel edges
		if (v1 == v2) or (v1 in M[v2]):
			#restart process if needed
			if (edgesTested == n*d):          
				repetitions=repetitions+1          
				edgesTested = 0
				stubs = list(range(n))*d
				M=[[] for i in range(n)]
		else:
			#add edge to graph
			M[v1].append(v2)
			M[v2].append(v1)
			#remove used half-edges
			i1,i2 = np.sort([i1,i2])
			stubs.pop(i2)
			stubs.pop(i1)
	if not isconnected(M):
		M = RRG_generate(n,d)
		#print('not connected')
	return(M)


def reduce_adj_mat(a):
	j=[]
	for i in range(len(a)):
		j.append(min(np.where(a[i][:])))
	return j

n = int(input('Enter the number of nodes '))
d = int(input('Enter the degree '))
number = int(input('Enter the number of graphs '))

for i in range(number):
	M = RRG_generate(n,d)
	print('Generated graph %d'%(i))
	#print(M)
	with open('./AdjMats/RRG/RRG_nodes_%d_deg_%d_no_%d.txt'%(n,d,i), 'w') as f:
		for item in M:
			f.write("%s\n" % item)




















