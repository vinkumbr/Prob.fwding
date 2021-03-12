#This file plots graphs taking data from simu_results.json
import matplotlib.pyplot as plt
import json

n = range(20,41)
m=101

#import from simu_results.json file
with open("doubletree_simu_results.json") as f:
	data = json.load(f)

height = data["height"]
k = data["k"]
pkndelta = data["pkndelta"]
tau_kndelta = data["tau_kndelta"]

fig1,ax1 = plt.subplots(1,1)
fig1.set_size_inches(5, 2.5)
#fig.suptitle('For a doubletree (two binary trees joined at the leaves) of height (root of one of the trees is the source and is at height 0; height is the level at which there are maximum nodes) given by the variable height. Probabilistic forwarding done with k=20 packets and delta = 0.1'% lbda)
ax1.plot(n,pkndelta,'o-')
ax1.set_title('Minimum forwarding probability')
plt.xlabel('Number of coded packets (n)')
plt.ylabel(r'$p_{\ k,n,\delta}$')
plt.tight_layout()
ax1.legend()

fig2,ax2 = plt.subplots(1,1)
fig2.set_size_inches(5, 2.5)
ax2.plot(n,tau_kndelta,'o-')
ax2.set_title('Expected number of transmissions')
plt.xlabel('Number of coded packets (n)')
plt.ylabel(r'$\tau_{\ k,n,\delta}$')
plt.tight_layout()
ax2.legend()
plt.show()

