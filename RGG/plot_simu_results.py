#This file plots graphs taking data from simu_results.json
import matplotlib.pyplot as plt
import json

n = range(20,41)
m=101

#import from simu_results.json file
with open("simu_results.json") as f:
	data = json.load(f)

lbda = data["lbda"]
pkndelta_simu = data["pkndelta_simu"]
pkndelta_simu1 = data["pkndelta_simu1"]
pkndelta_simu_big = data["pkndelta_simu_big"]
pkndelta_ergodic = data["pkndelta_ergodic"]
tau_kndelta_simu = data["tau_kndelta_simu"]
tau_kndelta_simu1 = data["tau_kndelta_simu1"]
tau_kndelta_simu_big = data["tau_kndelta_simu_big"]
tau_kndelta_ergodic = data["tau_kndelta_ergodic"]
tau_kndelta_pfs = data["tau_kndelta_pfs"]

tau_kndelta_simu = [tau/4.5 for tau in tau_kndelta_simu]
tau_kndelta_simu1 = [tau1/4 for tau1 in tau_kndelta_simu1]
tau_kndelta_pfs = [taupfs/4.5 for taupfs in tau_kndelta_pfs]
tau_kndelta_ergodic = [erg/4.5 for erg in tau_kndelta_ergodic]

fig1,ax1 = plt.subplots(1,1)
fig1.set_size_inches(5, 2.5)
#fig.suptitle('For an (instantiation of) RGG of intensity 4.5 spread in a 101 by 101 grid with connection radius =1. Probabilistic forwarding done with k=20 packets and delta = 0.1'% lbda)
ax1.plot(n,pkndelta_simu,'o-', label='$\lambda = 4.5$')
ax1.plot(n,pkndelta_simu1,'+--', label='$\lambda = 4$')
#ax1.plot(n,pkndelta_simu_big, label=r'$121 \times 121 $')
#ax1.plot(n,pkndelta_simu,'o-', label='from simulations')
#ax1.plot(n,pkndelta_ergodic,'+--', label='from heuristics')
#ax1.set_title('Minimum forwarding probability')
plt.xlabel('Number of coded packets (n)')
#plt.ylabel(r'$p_{\ k,n,\delta}$')
plt.tight_layout()
ax1.legend()

fig2,ax2 = plt.subplots(1,1)
fig2.set_size_inches(5, 2.5)
ax2.plot(n,tau_kndelta_simu,'o-', label='$\lambda = 4.5$')
ax2.plot(n,tau_kndelta_simu1,'+--', label='$\lambda = 4$')
#ax2.plot(n,tau_kndelta_simu_big, label=r'$121 \times 121$')
#ax2.plot(n,tau_kndelta_simu,'o-', label='from simulations')
#ax2.plot(n,tau_kndelta_ergodic,'+--',label='from heuristics')
#ax2.plot(n,tau_kndelta_pfs,'+--',label='using (9) with $p_{k,n,\delta}$ from Fig. 1(a)')
#ax2.set_title('Expected number of transmissions')
plt.xlabel('Number of coded packets (n)')
#plt.ylabel(r'$\tau_{\ k,n,\delta}\ / \ \lambda m^2$')
plt.tight_layout()
ax2.legend()
plt.show()

