# Inspired from https://breakingcode.wordpress.com/2013/04/08/finding-connected-components-in-a-graph/

from __future__ import division
from mpi4py import MPI
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
import numpy as np
import math
from array import *
from random import *
import sys
import json
#np.set_printoptions(threshold=np.nan)

import datetime
#print(start_time) 

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

#print(rank)

def createPPP(lbda,m):
	nodes=np.random.poisson(lbda*(m**2))
	l=m/2
	#u_1 = np.random.uniform(-l, l, nodes-1) 
	#u_2 = np.random.uniform(-l, l, nodes-1)
	u_1 = np.random.uniform(-l, l, nodes) 
	u_2 = np.random.uniform(-l, l, nodes) 
	z=[[0] for j in range(nodes)]
	#z[0]=complex(0,0)
	#for i in range(1,nodes):
		#z[i]=complex(u_1[i-1],u_2[i-1])
	for i in range(nodes):
		z[i]=complex(u_1[i],u_2[i])	
	return z,nodes

def createRGG(z,radius):
	M=[[] for i in range(len(z))]
	for i in range(len(z)):
		for j in range(i+1,len(z)):
			if (np.absolute(z[i]-z[j]))<=radius:
				M[i].append(j)
				M[j].append(i)
	return M

# The function to look for connected components.
def connected_components(M):
	nodes=len(M)
	# List of connected components found. The order is random.
	transmitters = []
	# Make a copy of the set, so we can modify it.
	number = nodes
	nodes = set(range(nodes))
	# Iterate while we still have nodes to process.
	while nodes:
		# Get a random node and remove it from the global set.
		n = nodes.pop()
		#print(n)
		#n=source
		# This set will contain the next group of nodes connected to each other.
		group = {n}
		source = {n}
		# Build a queue with this node in it.
		queue = [n]
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
		# Add the group to the list of groups.
		transmitters.append(group)
		if (len(group)>=number//2):
			#print("yes")
			break
	# Return the list of groups.
	#print(transmitters)
	#print(receivers)
	return transmitters

m=251
theta_lbda=[]
lbda_values=np.arange(2,2.1,0.01)

if rank==0:
	start_time = datetime.datetime.now()
	print(start_time)
for lbda in lbda_values:
	radius=1
	Phi,nodes=createPPP(lbda,m)
	M=createRGG(Phi,radius)
	T=np.zeros(1)
	nods=np.zeros(1)
	nodes=nods[0]+nodes
	transmitters=connected_components(M)
	indices=sorted(range(len(transmitters)), reverse=True, key=lambda k: len(transmitters[k]))
	T[0]=len(transmitters[indices[0]])
	if rank==0:
		Ttot=np.zeros(1)
		total_nodes = np.zeros(1)
	else:
		Ttot=None
		total_nodes = None
	comm.Barrier()
	comm.Reduce(T, Ttot, op=MPI.SUM, root=0)
	comm.Reduce(nodes,total_nodes,op=MPI.SUM,root=0)
	if rank==0:
		start_time = datetime.datetime.now()
		print(start_time)
		print(lbda)
		print(Ttot[0]/total_nodes[0])
		theta_lbda.append(Ttot[0]/total_nodes[0])
        	f= open("theta_lambda_%d.txt"%(m),'a')
		f.write(str(lbda)+'\n')
        	f.write(str(Ttot[0]/total_nodes[0])+'\n')
	        f.close()
if rank==0:
	print(lbda_values)
	print(theta_lbda)
	dict={"lbda":lbda_values,"theta_lambda":theta_lbda}
	json = json.dumps(dict)
	f= open("theta_lambda_%d.json"%(m),'a')
	f.write(json)
	f.close()











