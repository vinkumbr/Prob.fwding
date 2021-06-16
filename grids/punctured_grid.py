import json
import numpy as np
import matplotlib.pyplot as plt

# From simulations
k=20
delta=0.1
m = 31
n=range(20,41)

#Results of running prob_fwding_parallel.py on a grid with m=31 and delta = 0.1
pkndelta_simu = [0.82,0.75,0.72,0.7,0.686,0.677,0.669,0.665,0.661,0.6552,0.6512,0.6462,0.6444,0.6402,0.638,0.636,0.6331,0.6303,0.6288,0.6277,0.6252] 
tau_kndelta_simu = [15717.37, 14851.3, 14610.65, 14500.53, 14394.52, 14505.66, 14570.42, 14844.95, 14955.21, 14997.08, 14955.73, 15028.94, 15176.59, 15214.34, 15279.74, 15671.87, 15693.4, 15468.87, 15812.76, 16032.87, 15925.76]
tau_kndelta_simu = [i/m**2 for i in tau_kndelta_simu]
#Results of running prob_fwding_parallel.py on a punctured grid with m=31 and delta = 0.1 retaining every third row of edges
pkndelta_punc3 = [0.938,0.884,0.853,0.833,0.819,0.809,0.801,0.795,0.79,0.7852,0.7806,0.7776,0.775,0.7714,0.768,0.7664,0.7636,0.7612,0.7594,0.7576,0.7552]
tau_punc3 = [17941.87, 17454.74, 17226.24, 17124.39, 17162.06, 17185.37, 17195.74, 17554.98, 17533.95, 17811.51, 17789.61, 18001.21, 18274.14, 18275.9, 18347.42, 18735.69, 18498.36, 18565.5, 18976.4, 18937.38, 19080.57]
tau_punc3 = [i/m**2 for i in tau_punc3]

#Results of running prob_fwding_parallel.py on a punctured grid with m=31 and delta = 0.1 retaining every fifth row of edges
pkndelta_punc5 = [0.965,0.925,0.899,0.883,0.872,0.863,0.857,0.849,0.8445,0.841,0.837,0.8342,0.83,0.8272,0.8234,0.822,0.8196,0.8176,0.8162,0.8128,0.8112]
tau_punc5 = [18461.06, 18251.72, 18159.79, 18158.05, 18370.31, 18433.79, 18596.53, 18455.74, 18682.08, 18994.79, 19189.71, 19267.24, 19345.87, 19706.55, 19379.82, 19902.92, 19858.36, 19941.75, 20171.5, 20232.08, 20338.03]
tau_punc5 = [i/m**2 for i in tau_punc5]

#Results of running prob_fwding_parallel.py on a punctured grid with m=31 and delta = 0.1 retaining every fifth row of edges
pkndelta_punc15 = [0.99,0.974,0.963,0.956,0.949,0.944,0.9398,0.9355,0.9315,0.9285,0.9265,0.9238,0.921,0.9192,0.9172,0.916,0.9142,0.9118,0.9108,0.9089,0.9081]
tau_punc15 = [18957.62, 19196.91, 19412.27, 19698.38, 19850.86, 20079.41, 20390.63, 20481.15, 20653.15, 20757.2, 20949.21, 21330.42, 21435.79, 21575.25, 21891.82, 22217.64, 22296.18, 22312.38, 22569.61, 22653.73, 23194.81]
tau_punc15 = [i/m**2 for i in tau_punc15]

fig1,ax1 = plt.subplots(1,1)
fig1.set_size_inches(5, 2.5)
ax1.plot(n,pkndelta_simu,'o-', label='$G$')
ax1.plot(n,pkndelta_punc3,'+--', label='$G3$')
ax1.plot(n,pkndelta_punc5,'d-', label='$G5$')
ax1.plot(n,pkndelta_punc15,'s--', label='$G15$')
#ax1.set_title('Minimum forwarding probability')
plt.xlabel('Number of coded packets (n)')
plt.ylabel(r'$p_{\ k,n,\delta}$')
plt.tight_layout()
ax1.legend()

fig2,ax2 = plt.subplots(1,1)
fig2.set_size_inches(5, 2.5)
ax2.plot(n,tau_kndelta_simu,'o-', label='$G$')
ax2.plot(n,tau_punc3,'+--', label='$G3$')
ax2.plot(n,tau_punc5,'d-', label='$G5$')
ax2.plot(n,tau_punc15,'s--', label='$G15$')
#ax2.set_title('Expected number of transmissions')
plt.xlabel('Number of coded packets (n)')
plt.ylabel(r'$\tau_{\ k,n,\delta}\ / \ m^2$')
plt.tight_layout()
ax2.legend(loc=4)
plt.show()
