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
pkndelta_simu_big = data["pkndelta_simu_big"]
tau_kndelta_simu = data["tau_kndelta_simu"]
tau_kndelta_ergodic = data["tau_kndelta_ergodic"]
tau_kndelta_simu_big = data["tau_kndelta_simu_big"]

fig,(ax1,ax2) = plt.subplots(2,1)
fig.suptitle('For an (instantiation of) RGG of intensity %1.2f spread in a 101 by 101 grid with connection radius =1. Probabilistic forwarding done with k=20 packets and delta = 0.1'% lbda)
ax1.plot(n,pkndelta_simu,'o-', label='m=101')
ax1.plot(n,pkndelta_simu_big,'s-', label='m=121')
ax1.set_title('Minimum forwarding probability')
ax2.plot(n,tau_kndelta_simu,'o-', label='m=101')
ax2.plot(n,tau_kndelta_simu_big,'s-', label='m=121')
ax2.plot(n,tau_kndelta_ergodic,'+--',label='from theory')
ax2.set_title('Expected number of transmissions')
plt.xlabel('Number of coded packets (n)')

plt.legend()
plt.show()

