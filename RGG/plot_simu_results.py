#This file plots graphs taking data from simu_results.json
import matplotlib.pyplot as plt
import json
import numpy as np

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

with open("conf_intervals4.json") as p1:
	pdata1 = json.load(p1)
	ci1 = pdata1['conf_interval_pkndelta']
	ci1 = np.asarray(ci1)

with open("conf_intervals4-5.json") as p2:
	pdata2 = json.load(p2)
	ci2 = pdata2['conf_interval_pkndelta']
	ci2 = np.asarray(ci2)

with open("conf_intervals_tau4.json") as t1:
	tdata1 = json.load(t1)
	cit1 = tdata1['conf_interval_taukndelta']
	cit1 = np.asarray(cit1)

with open("conf_intervals_tau4-5.json") as t2:
	tdata2 = json.load(t2)
	cit2 = tdata2['conf_interval_taukndelta']
	cit2 = np.asarray(cit2)

with open("pfs_results.json") as pfs:
	pfs_data = json.load(pfs)
	tau_kndelta_pfs4 = pfs_data['tau_kndelta_pfs']

with open("heur_results.json") as heur:
	heur_data = json.load(heur)
	pkndelta_heur = heur_data['pkndelta_heur']
	tau_kndelta_heur = heur_data['tau_kndelta_heur']

fig1,ax1 = plt.subplots(1,1)
fig1.set_size_inches(5, 2.5)
#fig.suptitle('For an (instantiation of) RGG of intensity 4.5 spread in a 101 by 101 grid with connection radius =1. Probabilistic forwarding done with k=20 packets and delta = 0.1'% lbda)
#ax1.plot(n,pkndelta_simu,'o-', label='$\lambda = 4.5$')
#ax1.plot(n,pkndelta_simu1,'+--', label='$\lambda = 4$')
#ax1.errorbar(n,ci2[:,1],yerr=[ci2[:,1]-ci2[:,2],ci2[:,0]-ci2[:,1]],capsize=3,ls='-', label='$\lambda = 4.5$')
#ax1.errorbar(n,ci1[:,1],yerr=[ci1[:,1]-ci1[:,2],ci1[:,0]-ci1[:,1]],capsize=3,ls='--', label='$\lambda = 4$')

#ax1.plot(n,pkndelta_simu_big, label=r'$121 \times 121 $')
ax1.plot(n,ci2[:,1],'+-', label='from simulations')
#ax1.plot(n,ci1[:,1],'+-', label='from simulations',color='#ff7f0e')
ax1.plot(n,pkndelta_ergodic,'o--', label='from heuristics',color='#2ca02c')
#ax1.plot(n,pkndelta_heur,'o--', label='from heuristics',color='#2ca02c')
#ax1.set_title('Minimum forwarding probability')
plt.xlabel('Number of coded packets (n)')
#plt.ylabel(r'$p_{\ k,n,\delta}$')
plt.tight_layout()
ax1.legend()

fig2,ax2 = plt.subplots(1,1)
fig2.set_size_inches(5, 2.5)
#ax2.plot(n,tau_kndelta_simu,'+-', label='from simulations $\lambda = 4.5$')
#ax2.plot(n,tau_kndelta_simu1,'+--', label='$\lambda = 4$')
#ax2.plot(n,cit1[:,1],'+-', label='from simulations',color='#ff7f0e')
#ax2.errorbar(n,cit2[:,1],yerr=[cit2[:,2]-cit2[:,1],cit2[:,1]-cit2[:,0]],capsize=3,ls='-', label='from simulations')
#ax2.errorbar(n,cit1[:,1],yerr=[cit1[:,2]-cit1[:,1],cit1[:,1]-cit1[:,0]],capsize=3,ls='--', label='$\lambda = 4$')
#ax2.plot(n,tau_kndelta_simu_big, label=r'$121 \times 121$')
ax2.plot(n,cit2[:,1],'+-', label='from simulations')
ax2.plot(n,tau_kndelta_ergodic,'o--',label='from heuristics',color='#2ca02c')
#ax2.plot(n,tau_kndelta_heur,'o--',label='from heuristics',color='#2ca02c')
#ax2.plot(n,tau_kndelta_pfs,'o--',label='using (18) with $p_{k,n,\delta}$ from Fig. 1(a)',color='#2ca02c')
#ax2.plot(n,tau_kndelta_pfs4,'o--',label='using (18) with $p_{k,n,\delta}$ from Fig. 1(a)',color='#2ca02c')
#ax2.set_title('Expected number of transmissions')
plt.xlabel('Number of coded packets (n)')
#plt.ylabel(r'$\tau_{\ k,n,\delta}\ / \ \lambda m^2$')
plt.tight_layout()
ax2.legend()
plt.show()

