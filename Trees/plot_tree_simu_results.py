#This file plots graphs taking data from tree_simu_results.json
import matplotlib.pyplot as plt
import json
import numpy as np


#import from simu_results.json file
with open("bintree_simu_results.json") as f:
	data = json.load(f)

H=data['height']
n=data['n']
pkndelta_1 = data['pkndelta_1']
taukndelta_1 = data['taukndelta_1']
pkndelta_05 = data['pkndelta_05']
taukndelta_05 = data['taukndelta_05']

nodes = 2**(H+1)-1
taukndelta_1 = [i/nodes for i in taukndelta_1]
taukndelta_05 = [i/nodes for i in taukndelta_05]

fig1,ax1 = plt.subplots(1,1)
fig1.set_size_inches(5, 2)
#fig.suptitle('Probabilistic forwarding on a binary tree of height %d with k=100 packets'% H)
ax1.plot(n,pkndelta_1,'o-', label='$\delta = 0.1$')
ax1.plot(n,pkndelta_05,'+--', label='$\delta = 0.05$')
#ax1.set_title('Minimum retransmission probability')
ax1.set_ylabel(r'$p_{\ k,n,\delta}$')
plt.xlabel('Number of coded packets (n)')
#plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
plt.legend()
plt.figure
#plt.show()

fig2,ax2 = plt.subplots(1,1)
fig2.set_size_inches(5,2)
ax2.plot(n,taukndelta_1,'o-', label='$\delta = 0.1$')
ax2.plot(n,taukndelta_05,'+--', label='$\delta = 0.05$')
#ax2.plot(n,tau_kndelta_ergodic,'+--',label='from theory')
#ax2.set_title('Expected number of transmissions')
plt.xlabel('Number of coded packets (n)')
#plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
ax2.set_ylabel(r'$\tau_{ k,n,\delta} / N$')


plt.legend()
plt.show()
