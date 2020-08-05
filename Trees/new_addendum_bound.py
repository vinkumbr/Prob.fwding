from __future__ import division
from array import *
from scipy import special as sp
import numpy as np
import math

k=100
h=50
delta=0.1
deltap=delta*(2**(h+1)-1)/((2**(h+1))-2)
t=3*np.sqrt(k-1)/deltap**2
myt=-np.log(deltap)+np.sqrt(np.log(deltap)**2+2*(k-1))
newt=np.sqrt(2*(k-1)*(-np.log(deltap))+(np.log(deltap))**2)-np.log(deltap)
#p_lower = np.zeros(k+1)
#p_upper = np.zeros(k+1)
#start=k
#stop=2*k+1
p_lower = np.zeros(101)
p_upper = np.zeros(101)
start=100
stop=201
dummy=0
for N in range(start,stop):
	print (N)
	p_lower[dummy]=pow(((k-1)/N),1/(h-1))
	myt2=np.sqrt(-np.log(delta)*N/2)
	#p_lower[dummy]=pow((1/N),1/(h-1))
	p_upper[dummy]=min(pow((k-1+newt)/N,1/(h-1)),1)
	dummy=dummy+1
#r=np.arange(0,k+1,1)
n=np.arange(start,stop,1)
#trans_lower=((pow(2*p_lower,h)-1)/(2*p_lower-1))*(r+k)
#trans_upper=((pow(2*p_upper,h)-1)/(2*p_upper-1))*(r+k)
trans_lower=((pow(2*p_lower,h+1)-1)/(2*p_lower-1))*(n)
trans_upper=((pow(2*p_upper,h+1)-1)/(2*p_upper-1))*(n)
f=open('prob_lower_approx.txt','w')
g=open('prob_upper_approx.txt','w')
t=open('trans_lower_approx.txt','w')
u=open('trans_upper_approx.txt','w')
for i in range(len(n)):
	f.write("%f,"%p_lower[i])
	g.write("%f,"%p_upper[i])
	t.write("%f,"%trans_lower[i])
	u.write("%f,"%trans_upper[i])
f.close()
g.close()
t.close()
u.close()
