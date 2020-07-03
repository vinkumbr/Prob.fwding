from __future__ import division
from mpi4py import MPI
import numpy as np
import math
from array import *
from random import *
import sys
import datetime
import matplotlib.pyplot as plt

# Python program to convert a list 
# of character 
def convert(s): 
	# initialization of string to "" 
	str1 = "" 
	# using join function join the list s by  
	# separating words by str1 
	return(str1.join(s)) 

m = 101
lbda = 4.5
fig,ax = plt.subplots(1,1)
for i in range(1,10):
	M = []
	with open('./AdjMats/RGG4.5_average/RGG%d_%d_int_%s.txt'%(i,m,lbda), 'r') as f:
		for line in f:
			newPlace=[]
			currentPlace = line[1:-2]
			r=convert(currentPlace)
			s=r.split(', ')
			newPlace=[int(e) for e in s ]
			M.append(newPlace)
	max_deg = max([len(M[i]) for i in range(len(M))])
	deg_dist = np.zeros(max_deg)
	for i in range(len(M)):
		deg_dist[len(M[i])] = deg_dist[len(M[i])]+1
	ax.plot(range(max_deg),deg_dist,label = "Trace %d"%i)

plt.xlabel('Degree')
plt.legend()
plt.show()
