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

M = []
with open('./AdjMats/test_formula/RGG_101_int_4.5_id_%d.txt'%(rank),'r') as f:
	for line in f:
		newPlace=[]
		currentPlace = line[1:-2]
		r=convert(currentPlace)
		s=r.split(', ')
		try:
			newPlace=[int(e) for e in s]
		except:
			newPlace=[]
		M.append(newPlace)

nodes=len(M)
# This is the pkndelta values obtained using the prob_fwding_parallel.py code on RGG_M.txt
pkndelta = [0.33,0.34,0.35,0.36,0.37,0.38,0.39,0.4,0.41,0.42,0.43,0.44,0.45]
k=1
iterations = 100
tau = np.zeros(len(pkndelta))
tau_kndelta = np.zeros(len(pkndelta))
for l in range(len(pkndelta)):
	if rank == 0:
		print(datetime.datetime.now())
		print(l)
	n=k
	p=pkndelta[l]
	trans = np.zeros(len(pkndelta))
	for i in range(iterations):
		transmitters={}
		receivers={}
		unif_mat=[random() for r in range(nodes)]
		b=np.zeros(nodes)
		for r in range(1,nodes):
			b[r]=(unif_mat[r]<p)
		b[0]=1 # // takes the floor value
		[transmitters,receivers]=connected_components(nodes,M,b)
		trans[l] = trans[l]+len(list(transmitters[0]))
	if rank==0:
		print(trans[l]/iterations)
	tau[l] = trans[l]/iterations
comm.Barrier()
recvbuf = None
if rank == 0:
	recvbuf = np.zeros([size,len(pkndelta)])
comm.Gather(tau,recvbuf,root=0)
comm.Reduce(tau, tau_kndelta, op=MPI.SUM, root=0)
if rank==0:
	start_time = datetime.datetime.now()
	print(start_time)
	tau_kndelta = tau_kndelta/size
	print(tau_kndelta)
	f=open('./AdjMats/test_formula/trans_average_single_pkt.txt','a')
	f.write(str(pkndelta)+'\n')
	f.write(str(tau_kndelta)+'\n')
	f.write(str(datetime.datetime.now())+'\n')
	for i in range(size):
		    f.write(str(recvbuf[i,:])+'\n')
	f.close()

