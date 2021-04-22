import json
import numpy as np
import scipy.special as sp
from scipy.stats import binom
from scipy.interpolate import interp1d

def binomial(n, k):
    if not 0 <= k <= n:
        return 0
    b = 1
    for t in range(min(k, n-k)):
        b *= n
        b //= t+1
        n -= 1
    return b

# From simulations
k=20
delta=0.1
m= 31
#n=20:1:40
print('Input the size of the grid ')# and size m (101 or 121)')
lbda = float(input('m '))
#Results of running prob_fwding_parallel.py on a grid with m=31 and delta =0.1
pkndelta_simu = [0.82,0.75,0.72,0.7,0.686,0.677,0.669,0.665,0.661,0.6552,0.6512,0.6462,0.6444,0.6402,0.638,0.636,0.6331,0.6303,0.6288,0.6277,0.6252] 
tau_kndelta_simu = [15717.37, 14851.3, 14610.65, 14500.53, 14394.52, 14505.66, 14570.42, 14844.95, 14955.21, 14997.08, 14955.73, 15028.94, 15176.59, 15214.34, 15279.74, 15671.87, 15693.4, 15468.87, 15812.76, 16032.87, 15925.76]

#Ergodic result
lbda_pkndelta = [lbda*p for p in pkndelta_simu]

#import from json file
with open("theta_thetaplus.json") as f:
	data = json.load(f)

# The lambda values in the file are from 1 to 4.99 in steps of 0.01
p = data["p"]
thetap = data["thetap"]
thetaplus = data["thetaplus"]

p_fine = np.arange(0.45,1,0.000001)
p_sq = p*p
thetap_sq = thetap**2
thetaplus_sq = thetap_sq/p_sq
func = interp1d(p,thetaplus_sq)
thetaplus_sq_fine = func(p_fine)

index = 0
print(k)
pkndelta_ergodic = np.zeros(k+1)
n=k
while n<=40:
	minp_index = 0
	prob_cdf = np.zeros(len(p_fine))
	prob_sum = np.zeros(len(p_fine))
	for j in range(k):
		prob_sum = binomial(n,j)*thetaplus_sq_fine**j*(1-thetaplus_sq_fine)**(n-j)
		prob_cdf = prob_cdf+prob_sum
	#prob = lbda*(binom.cdf(k-1,n,theta_lbda_p**2))
	try:
		minp_index = min(np.where(prob_cdf<=delta)[0])
	except:
		minp_index = -1
	pkndelta_ergodic[index] = p_fine[minp_index]
	#print(minp_index) 
	index = index+1
	n=n+1
print(pkndelta_ergodic)
#prob_from_simu = np.array(pkndelta_simu)
#thetaplus_pfs = f(lbda*prob_from_simu)
#tau_kndelta_pfs = lbda*prob_from_simu*thetaplus_pfs**2*np.arange(k,k+len(prob_from_simu))
thetaplus_pkndelta = func(pkndelta_ergodic)
tau_kndelta_ergodic = thetaplus_pkndelta**2*np.arange(k,k+len(pkndelta_ergodic))/pkndelta_ergodic

#print(pkndelta_ergodic)
#print(tau_kndelta_ergodic)

dict={"lbda":lbda,"pkndelta_simu":pkndelta_simu,"pkndelta_ergodic":list(pkndelta_ergodic),"tau_kndelta_simu":tau_kndelta_simu,"tau_kndelta_ergodic":list(tau_kndelta_ergodic)}
json = json.dumps(dict)
f= open("simu_results.json","w")
f.write(json)
f.close()

