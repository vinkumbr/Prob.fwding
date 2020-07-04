from __future__ import division
import numpy as np
import math
from array import *
from random import *
import sys
import datetime
import matplotlib.pyplot as plt
from scipy.stats import poisson

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
	deg_dist = np.zeros(max_deg+1)
	for j in range(len(M)):
		deg_dist[len(M[j])] = deg_dist[len(M[j])]+1
	deg_dist = deg_dist/len(M)
	ax.plot(range(max_deg+1),deg_dist,label = "Trace %d"%i)
ax.plot(range(max_deg+1),poisson.pmf(range(max_deg+1),lbda*np.pi),'--',label='Poisson')

plt.xlabel('Degree')
plt.legend()
plt.show()
