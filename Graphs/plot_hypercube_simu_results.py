#This file plots graphs taking data from simu_results.json
import matplotlib.pyplot as plt
import json


#import from simu_results.json file
with open("hypercube_simu_results.json") as f:
	data = json.load(f)

d = data["d"]
pkndelta = data["pkndelta"]
tau_kndelta = data["tau_kndelta"]
d1 = data["d1"]
pkndelta1 = data["pkndelta1"]
tau_kndelta1 = data["tau_kndelta1"]
pkndelta_long = data["pkndelta_long"]
tau_kndelta_long = data["tau_kndelta_long"]
pkndelta1_long = data["pkndelta1_long"]
tau_kndelta1_long = data["tau_kndelta1_long"]

#n = range(20,20+len(pkndelta))
n = range(200,710,50)

tau_kndelta = [i/2**int(d) for i in tau_kndelta]
tau_kndelta1 = [i/2**int(d1) for i in tau_kndelta1]
tau_kndelta_long = [i/2**int(d) for i in tau_kndelta_long]
tau_kndelta1_long = [i/2**int(d1) for i in tau_kndelta1_long]

fig1,ax1 = plt.subplots(1,1)
fig1.set_size_inches(5, 2.5)
#fig.suptitle('For a hypercube with 2^12 nodes, r bit vertices or r neighbors. Probabilistic forwarding done with k=20 packets and delta = 0.1)
#ax1.plot(n,pkndelta,'o-', label='$d =12$')
#ax1.plot(n,pkndelta1,'+--', label='$d = 10$')
ax1.plot(n,pkndelta_long,'o-', label='$d =12$')
ax1.plot(n,pkndelta1_long,'+--', label='$d = 10$')
#ax1.set_title('Minimum forwarding probability')
plt.xlabel('Number of coded packets (n)')
plt.ylabel(r'$p_{\ k,n,\delta}$')
plt.tight_layout()
ax1.legend()

fig2,ax2 = plt.subplots(1,1)
fig2.set_size_inches(5, 2.5)
#ax2.plot(n,tau_kndelta,'o-',label='$d = 12$')
#ax2.plot(n,tau_kndelta1,'+--',label='$d = 10$')
ax2.plot(n,tau_kndelta_long,'o-',label='$d = 12$')
ax2.plot(n,tau_kndelta1_long,'+--',label='$d = 10$')
#ax2.set_title('Expected number of transmissions')
plt.xlabel('Number of coded packets (n)')
plt.ylabel(r'$\tau_{\ k,n,\delta} / N$')
plt.tight_layout()
ax2.legend()
plt.show()

