# Inspired from https://breakingcode.wordpress.com/2013/04/08/finding-connected-components-in-a-graph/

from __future__ import division
from mpi4py import MPI
import numpy as np
import math
from array import *
from random import *
import sys
#np.set_printoptions(threshold=np.nan)

import datetime
start_time = datetime.datetime.now()
#print(start_time) 

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

#print(rank)

# The function to look for connected components.
def connected_components(nodes,M,b):
	# List of connected components found. The order is random.
	transmitters = []
	receivers=[]
	# Make a copy of the set, so we can modify it.
	number = nodes
	nodes = set(range(nodes))
	source = number//2
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
		for i in range(len(M[0])):
			if (M[n][i]!=-1) and (b[M[n][i]]==1):
				neighbors.append(M[n][i])
			if (M[n][i]!=-1) and (b[M[n][i]]==0):
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


if rank==0:
	m=31 #keep this to be odd 
	nodes= m*m
	lat_type='t'
	if lat_type == 's':
		M=np.zeros((nodes,4),dtype=np.int)   #stores the reduced adjacency matrix with the M(x,0) the east neighbor; M(x,1) the north neighbor; M(x,2) the west neighbor of x. Entry=-1 when there is no neighbor
		for i in range(nodes):
			if i%m!=m-1:
				M[i][0]=i+1
			else:
				M[i][0]=-1
			if i<=m*m-m-1:
				M[i][1]=i+m
			else:
				M[i][1]=-1
			if i%m!=0:
				M[i][2]=i-1
			else:
				M[i][2]=-1
			if i>=m:
				M[i][3]=i-m
			else:
				M[i][3]=-1
		#print (M)                 # Note: bottom left vertex has index 0
	elif lat_type == 't':
		M=np.zeros((nodes,6),dtype=np.int)   #stores the reduced adjacency matrix with the M(x,0) the east neighbor; M(x,1) the north neighbor; M(x,2) the west neighbor of x. Entry=-1 when there is no neighbor
		for i in range(nodes):
			if i%m!=m-1:
				M[i][0]=i+1
				if i<=m*m-m-1:
					M[i][4]=i+m+1
				else:
					M[i][4]=-1
			else:
				M[i][0]=-1
				M[i][4]=-1
			if i<=m*m-m-1:
				M[i][1]=i+m
			else:
				M[i][1]=-1
			if i%m!=0:
				M[i][2]=i-1
				if i>=m:
					M[i][5]=i-m-1
				else:
					M[i][5]=-1
			else:
				M[i][2]=-1
				M[i][5]=-1
			if i>=m:
				M[i][3]=i-m
			else:
				M[i][3]=-1
		#print (M)                 # Note: bottom left vertex has index 0
else:
	M=None

M=comm.bcast(M,root=0)
nodes=len(M)
q=0
start= 0.5496
stop=0.5
step=0.0001
p=start
k=20
delta=0.05
n=40
if rank==0:
	print(n)
iter=size
recs=[]

while p>stop:
	R_succ=np.zeros(1)
	R=np.zeros(nodes)
	for i in range(n):
		transmitters={}
		receivers={}
		unif_mat=[random() for r in range(nodes)]
		b=np.zeros(nodes)
		for r in range(1,nodes):
			b[r]=(unif_mat[r]<p)
		b[0]=1 # // takes the floor value
		[transmitters,receivers]=connected_components(nodes,M,b)
		#print(list(transmitters[0]))
		R[list(receivers[0])]+=1
		R[list(transmitters[0])]+=1
	R_succ[0]=len(R[R>=k])
	ER_succ=np.zeros(1)
	comm.Barrier()
	comm.Reduce(R_succ, ER_succ, op=MPI.SUM, root=0)
	if rank==0:
		start_time = datetime.datetime.now()
		print(p)
		print(start_time)
		recs.append(ER_succ[0]/(iter*nodes))
		print(recs[q])
		if recs[q]<(1-delta):
			break
	p=p-step
	q=q+1
if rank==0:
	f=open('pkndelta.txt','a')
	f.write(str(k)+'\n')
	f.write(str(n)+'\n')
	f.write(str(p+step)+'\n')
	f.write(str(datetime.datetime.now())+'\n')
	print(k)
	print(n)
	print(p+step)
	print(datetime.datetime.now())
	f.close()



