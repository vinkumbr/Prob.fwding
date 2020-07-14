
from __future__ import division

import numpy as np
from mpi4py import MPI
import math
from array import *
from random import *
import sys
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
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
	print(lbda*(m**2))
	nodes=int(np.ceil(lbda*(m**2)))
	l=m/2
	u_1 = np.random.uniform(-l, l, nodes-1) 
	u_2 = np.random.uniform(-l, l, nodes-1)
	z=[[0] for j in range(nodes)]
	z[0]=complex(0,0)
	for i in range(1,nodes):
		z[i]=complex(u_1[i-1],u_2[i-1])
	return z

def createRGG(z,radius):
	print(rank)
	M=[[] for i in range(len(z))]
	for i in range(len(z)):
		for j in range(i+1,len(z)):
			if (np.absolute(z[i]-z[j]))<=radius:
				M[i].append(j)
				M[j].append(i)
	return M

def generatevalidRGG(lbda,m,radius):
	Phi=createPPP(lbda,m)
	#with open('./AdjMats/test_formula/RGGlocs_%d_int_%s.txt'%(m,lbda), 'w') as f:
	#	for item in Phi:
	#		f.write("%s\n" % item)
	M=createRGG(Phi,radius)
	with open('./AdjMats/test_formula/RGG_%d_int_%s_id_%d.txt'%(m,lbda,rank), 'w') as f:
		for item in M:
			f.write("%s\n" % item)

if rank ==0:
	print('Input lambda, size of grid (m) and the radius ')
	lbda=float(input('lambda '))
	m=int(input('m '))
	radius=float(input('radius '))
else:
	lbda = 0
	m = 101
	radius = 1

lbda = comm.bcast(lbda,root=0)
m = comm.bcast(m,root=0)
radius = comm.bcast(radius,root=0)

generatevalidRGG(lbda,m,radius)


