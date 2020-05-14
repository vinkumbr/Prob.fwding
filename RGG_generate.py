
from __future__ import division
from mpi4py import MPI
import numpy as np
import math
from array import *
from random import *
import sys
np.set_printoptions(threshold=np.nan)

import datetime
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

def createPPP(lbda,m):
	nodes=int(np.ceil(lbda*(m**2)))
	l=m/2
	u_1 = np.random.uniform(-l, l, nodes-1) 
	u_2 = np.random.uniform(-l, l, nodes-1)
	#u_1 = np.random.uniform(-l, l, nodes) 
	#u_2 = np.random.uniform(-l, l, nodes) 
	z=[[0] for j in range(nodes)]
	z[0]=complex(0,0)
	for i in range(1,nodes):
		z[i]=complex(u_1[i-1],u_2[i-1])
	#for i in range(nodes):
		#z[i]=complex(u_1[i],u_2[i])	
	return z

def createRGG(z,radius):
	M=[[] for i in range(len(z))]
	for i in range(len(z)):
		for j in range(i+1,len(z)):
			if (np.absolute(z[i]-z[j]))<=radius:
				M[i].append(j)
				M[j].append(i)
	return M

def generatevalidRGG(lbda,m,radius):
	while True:
		Phi=createPPP(lbda,m)
		M=createRGG(Phi,radius)
		if isconnected(M):
			print('RGG generated')
			break
		else:
			print('not connected')
	return(M)

print('Input lambda, size of grid (m) and the radius')
lbda=input('lambda')
m=input('m')
radius=input('radius')
M=generatevalidRGG(lbda,m,radius)
with open('RGG_M.txt', 'w') as f:
    for item in M:
        f.write("%s\n" % item)
