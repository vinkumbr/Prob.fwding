# Inspired from https://breakingcode.wordpress.com/2013/04/08/finding-connected-components-in-a-graph/

from __future__ import division
from mpi4py import MPI
import numpy as np
import math
from array import *
from random import *
import sys


import datetime

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


# Python program to convert a list 
# of character 
  
def convert(s): 
  
    # initialization of string to "" 
    str1 = "" 
  
    # using join function join the list s by  
    # separating words by str1 
    return(str1.join(s)) 

num_graphs = 20
RGGid = rank%num_graphs
M = []
with open('./AdjMats/RRG/RRG_nodes_1000_deg_4_no_%d.txt'%(RGGid),'r') as f:
	for line in f:
		newPlace=[]
		currentPlace = line[1:-2]
		r=convert(currentPlace)
		s=r.split(', ')
		newPlace=[int(e) for e in s ]
		M.append(newPlace)

nodes=len(M)
q=0
# This is the pkndelta values obtained using the prob_fwding_parallel.py code on RGG_M.txt
pkndelta = [0.8,0.7,0.64,0.61,0.588,0.564,0.55,0.53,0.518,0.509,0.5038,0.4982,0.4918,0.4854,0.4808, 0.4759,0.4728,0.4691,0.4651,0.4616]
k=20
iter=size
if rank==0:
	tau_kndelta = []
	#print(n)
	print(iter)
for l in range(len(pkndelta)):
	tau = np.zeros(1)
	n=k+l
	p=pkndelta[l]
	trans = np.zeros(1)
	for i in range(n):
		transmitters={}
		receivers={}
		unif_mat=[random() for r in range(nodes)]
		b=np.zeros(nodes)
		for r in range(1,nodes):
			b[r]=(unif_mat[r]<p)
		b[0]=1 # // takes the floor value
		[transmitters,receivers]=connected_components(nodes,M,b)
		trans[0] = trans[0]+len(list(transmitters[0]))
	comm.Barrier()
	comm.Reduce(trans, tau, op=MPI.SUM, root=0)
	if rank==0:
		start_time = datetime.datetime.now()
		print(p)
		print(n)
		print(start_time)
		tau_kndelta.append(tau[0]/(iter))
		print(tau_kndelta[q])
	q=q+1
if rank==0:
	f=open('tau_kndelta_avg.txt','a')
	f.write(str(k)+'\n')
	#f.write(str(n)+'\n')
	f.write(str(tau_kndelta)+'\n')
	f.write(str(datetime.datetime.now())+'\n')
	print(k)
	print(nodes)
	print(tau_kndelta)
	#print(n)
	#print(p+step)
	print(datetime.datetime.now())
	f.close()

