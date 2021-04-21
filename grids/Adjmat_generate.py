
from __future__ import division

import numpy as np
import math
from array import *
from random import *
import sys

import datetime
def gridadjmat(n):
	size=n*n
	a=np.zeros((size,size))
	for i in range(size):
		if i>=n:
			a[i][i-n]=1
		if i%n!=0:
			a[i][i-1]=1
	a=a+np.matrix.transpose(a)
	return a

def reduce_adj_mat(a):
	j=[]
	for i in range(len(a)):
		j.append(min(np.where(a[i][:])))
	return j

def generate_grid(m):
	return(reduce_adj_mat(gridadjmat(m)))

print('Input size of grid (m)')
m=int(input('m '))
M=generate_grid(m)
with open('./AdjMats/grid_%d.txt'%(m), 'w') as f:
    for item in M:
        f.write("%s\n" % item)
