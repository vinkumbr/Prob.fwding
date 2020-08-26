#This file plots graphs taking data from bintree_approx_results.json
import matplotlib.pyplot as plt
import json
import numpy as np


#import from simu_results.json file
with open("bintree_approx_results.json") as f:
	data = json.load(f)

n = data['n']
minp_expr = data['minp_expr']
trans_expr = data['trans_expr'] 
upper_tight = data['upper_tight']
tau_upper_tight = data['tau_upper_tight']
lower_tight = data['lower_tight']
tau_lower_tight = data['tau_lower_tight']
lower_approx = data['lower_approx']
trans_lower_approx = data['trans_lower_approx']
upper_approx = data['upper_approx']
trans_upper_approx = data['trans_upper_approx']

fig1,ax1 = plt.subplots(1,1)
fig1.set_size_inches(5, 2.3)
#fig.suptitle('Probabilistic forwarding on a binary tree of height 50 with k=100 packets'% H)
ax1.plot(n,upper_approx,'g|', label='upper bound from Prop V.2',ms=4)
ax1.plot(n,upper_tight,'r:', label='upper bound from (5)',lw=3)
ax1.plot(n,minp_expr,'b-', label='numerically solving (4)',lw=2)
ax1.plot(n,lower_tight,'r--', label='lower bound from (6)',lw=2)
ax1.plot(n,lower_approx,'g+', label='lower bound from Prop V.1',ms=2.5)

#ax1.set_title('Minimum retransmission probability')
ax1.set_ylabel(r'$p_{\ k,n,\delta}$')
plt.xlabel('Number of coded packets (n)')
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
plt.legend(prop={'size': 6})
plt.tight_layout()
plt.figure
#plt.show()

fig2,ax2 = plt.subplots(1,1)
fig2.set_size_inches(5,2.3)
ax2.plot(n,trans_upper_approx,'g|', label='upper bound using Prop V.2',ms=5)
ax2.plot(n,tau_upper_tight,'r:', label='upper bound using (5)',lw=3)
ax2.plot(n,trans_expr,'b-', label='numerically solving (4)',lw=2)
ax2.plot(n,tau_lower_tight,'r--', label='lower bound using (6)',lw=2)
ax2.plot(n,trans_lower_approx,'g+', label='lower bound using Prop V.1',ms=2.5)

#ax2.plot(n,tau_kndelta_ergodic,'+--',label='from theory')
#ax2.set_title('Expected number of transmissions')

plt.xlabel('Number of coded packets (n)')
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
ax2.set_ylabel(r'$\tau_{ k,n,\delta}$')


plt.legend(prop={'size': 6})
plt.tight_layout()
plt.show()
