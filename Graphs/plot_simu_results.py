#This file plots graphs taking data from simu_results.json
import matplotlib.pyplot as plt
import json


#import from simu_results.json file
with open("doubletree_simu_results.json") as f:
	data = json.load(f)

height = data["height"]
k = data["k"]
pkndelta = data["pkndelta"]
tau_kndelta = data["tau_kndelta"]

print(k)
print(height)
N = 3*2**height-2
tau_kndelta = [i/N for i in tau_kndelta]
if int(k) == 20:
	n = range(20,41)
elif int(k) == 100:
	n = range(100,201,10)

fig1,ax1 = plt.subplots(1,1)
fig1.set_size_inches(5, 2.5)
#fig.suptitle('For a doubletree (two binary trees joined at the leaves) of height (root of one of the trees is the source and is at height 0; height is the level at which there are maximum nodes) given by the variable height. Probabilistic forwarding done with k=20 packets and delta = 0.1'% lbda)
ax1.plot(n,pkndelta,'o-', label='$\delta=0.1$')
#ax1.set_title('Minimum forwarding probability')
plt.xlabel('Number of coded packets (n)')
plt.ylabel(r'$p_{\ k,n,\delta}$')
plt.tight_layout()
ax1.legend()

fig2,ax2 = plt.subplots(1,1)
fig2.set_size_inches(5, 2.5)
ax2.plot(n,tau_kndelta,'o-',label='$\delta=0.1$')
#ax2.set_title('Expected number of transmissions')
plt.xlabel('Number of coded packets (n)')
plt.ylabel(r'$\tau_{\ k,n,\delta} / N$')
plt.tight_layout()
ax2.legend()
plt.show()

