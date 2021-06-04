#This file plots graphs taking data from simu_results.json
import matplotlib.pyplot as plt
import json



#import from simu_results.json file
with open("simu_results.json") as f:
	data = json.load(f)

m = data["m"]
k = data["k"]
pkndelta_simu = data["pkndelta_simu"]
pkndelta_simu1 = data["pkndelta_simu1"]
#pkndelta_simu_big = data["pkndelta_simu_big"]
pkndelta_ergodic = data["pkndelta_ergodic"]
tau_kndelta_simu = data["tau_kndelta_simu"]
tau_kndelta_simu1 = data["tau_kndelta_simu1"]
#tau_kndelta_simu_big = data["tau_kndelta_simu_big"]
tau_kndelta_ergodic = data["tau_kndelta_ergodic"]
#tau_kndelta_pfs = data["tau_kndelta_pfs"]

n = range(k,2*k+1)

fig1,ax1 = plt.subplots(1,1)
fig1.set_size_inches(5, 2.5)
#fig.suptitle('For an (instantiation of) RGG of intensity 4.5 spread in a 101 by 101 grid with connection radius =1. Probabilistic forwarding done with k=20 packets and delta = 0.1'% lbda)
ax1.plot(n,pkndelta_simu,'o-', label='$\delta = 0.1$')
ax1.plot(n,pkndelta_simu1,'+--', label='$\delta = 0.05$')
#ax1.plot(n,pkndelta_simu_big, label=r'$121 \times 121 $')
#ax1.plot(n,pkndelta_simu,'o-', label='$\delta = 0.1$')
#ax1.plot(n,pkndelta_ergodic,'+--', label='from theory')
#ax1.set_title('Minimum forwarding probability')
plt.xlabel('Number of coded packets (n)')
plt.ylabel(r'$p_{\ k,n,\delta}$')
plt.tight_layout()
ax1.legend()

fig2,ax2 = plt.subplots(1,1)
fig2.set_size_inches(5, 2.5)
ax2.plot(n,tau_kndelta_simu,'o-', label='$\delta = 0.1$')
ax2.plot(n,tau_kndelta_simu1,'+--', label='$\\delta = 0.05$')
#ax2.plot(n,tau_kndelta_simu_big, label=r'$121 \times 121$')
#ax2.plot(n,tau_kndelta_simu,'o-', label='from simulations')
#ax2.plot(n,tau_kndelta_ergodic,'+--',label='from theory')
#ax2.plot(n,tau_kndelta_pfs,'+--',label='using prob from simu')
#ax2.set_title('Expected number of transmissions')
plt.xlabel('Number of coded packets (n)')
plt.ylabel(r'$\tau_{\ k,n,\delta}\ / \ m^2$')
plt.tight_layout()
ax2.legend()
plt.show()

