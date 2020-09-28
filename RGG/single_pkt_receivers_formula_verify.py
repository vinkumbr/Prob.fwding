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
def connected_components(nodes,M,b):
	# List of connected components found. The order is random.
	transmitters = []
	receivers=[]
	# Make a copy of the set, so we can modify it.
	number = nodes
	nodes = set(range(nodes))
	source = 0
	# This set will contain the next group of nodes connected to each other.
	group = {source}
	rgroup = {source}
	# Build a queue with this node in it.
	queue = [source]
	source = {source}
	# Iterate the queue.
	# When it's empty, we finished visiting a group of connected nodes.
	while queue:
		# Consume the next item from the queue.
		n = queue.pop(0)
		# Fetch the neighbors.
		neighbors=[]
		recd=[]
		for i in range(len(M[n])):
			if b[M[n][i]]==1:
				neighbors.append(M[n][i])
			if b[M[n][i]]==0:
				recd.append(M[n][i])
		#neighbors = n.links
		# converting it to a set
		neighbors=set(neighbors)
		recd=set(recd)
		# Remove the neighbors we already visited.
		neighbors.difference_update(group)
		recd.difference_update(rgroup)
		# Remove the remaining nodes from the global set.
		nodes.difference_update(neighbors)
		# Add them to the group of connected nodes.
		group.update(neighbors)
		rgroup.update(recd)
		# Add them to the queue, so we visit them in the next iterations.
		queue.extend(neighbors)
		#print(queue)
	# Add the group to the list of groups.
	rgroup.difference_update(source)
	transmitters.append(group)
	receivers.append(rgroup)
	# Return the list of groups.
	return transmitters,receivers

m=251
lbda = 4.5
p_values = np.arange(0.33,0.5,0.005)

if rank==0:
	start_time = datetime.datetime.now()
	print(start_time)
	recs = []
for p in p_values:
	radius=1
	Phi,nodes=createPPP(lbda,m)
	M=createRGG(Phi,radius)
	T=np.zeros(1)
	R=np.zeros(1)
	TR = np.zeros(1)
	nods=np.zeros(1)
	nodes=nods[0]+nodes
	b=np.zeros(nodes)
	for r in range(1,nodes):
		b[r]=(unif_mat[r]<p)
	b[0]=1 # // takes the floor value
	transmitters,receivers = connected_components(nodes,M,b)
	indices=sorted(range(len(transmitters)), reverse=True, key=lambda k: len(transmitters[k]))
	T[0] = len(transmitters[indices[0]])
	R[0] = len(receivers[0])
	TR[0] = T[0]+R[0]
	if rank==0:
		TRtot=np.zeros(1)
		total_nodes = np.zeros(1)
	else:
		TRtot=None
		total_nodes = None
	comm.Barrier()
	comm.Reduce(TR, TRtot, op=MPI.SUM, root=0)
	comm.Reduce(nodes,total_nodes,op=MPI.SUM,root=0)
	if rank==0:
		start_time = datetime.datetime.now()
		print(start_time)
		print(p)
		print(TRtot[0]/total_nodes[0]/size)
		recs.append(TRtot[0]/size)
		f= open("single_pkt_recs.txt",'a')
		f.write(str(p)+'\n')
		f.write(str(TRtot[0]/total_nodes[0]/size)+'\n')
		f.close()
if rank==0:
	print(p_values)
	print(recs_lbda)
	dict={"lbda":lbda,"p":p_values,"recs":recs,"total_nodes":total_nodes}
	json = json.dumps(dict)
	f= open("single_pkt_recs.json"%(m),'a')
	f.write(json)
	f.close()











