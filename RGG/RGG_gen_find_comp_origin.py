
from __future__ import division

import numpy as np
import math
from array import *
from random import *
import sys

import datetime
def find_comp_origin(M):
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
	comp_origin = list(group)
	#print(len(nodes))
	return(comp_origin)

def createPPP(lbda,m):
	#nodes=int(np.ceil(lbda*(m**2)))
	nodes=np.random.poisson(lbda*(m**2))
	l=m/2
	u_1 = np.random.uniform(-l, l, nodes-1) 
	u_2 = np.random.uniform(-l, l, nodes-1)
	z=[[0] for j in range(nodes)]
	z[0]=complex(0,0)
	for i in range(1,nodes):
		z[i]=complex(u_1[i-1],u_2[i-1])
	return z

def createRGG(z,radius):
	M=[[] for i in range(len(z))]
	for i in range(len(z)):
		for j in range(i+1,len(z)):
			if (np.absolute(z[i]-z[j]))<=radius:
				M[i].append(j)
				M[j].append(i)
	return M

def generatevalidRGG(lbda,m,radius,number):
	i = 0
	while i<number:
		print(i)
		Phi=createPPP(lbda,m)
		#print(len(Phi))
		M=createRGG(Phi,radius)
		comp_origin = find_comp_origin(M)
		Phi_origin = [Phi[i] for i in comp_origin]
		print(len(Phi_origin))
		M=createRGG(Phi_origin,radius)
		with open('./AdjMats/comp_origin/RGG_%d_int_%s_id_%d.txt'%(m,lbda,i), 'w') as f:
			for item in M:
				f.write("%s\n" % item)
		i=i+1

print('Input lambda, size of grid (m), radius and the number of graphs you want')
lbda=input('lambda ')
m=input('m ')
radius=input('radius ')
lbda=float(lbda)
m=int(m)
radius=float(radius)
number=int(input('number'))
generatevalidRGG(lbda,m,radius,number)
