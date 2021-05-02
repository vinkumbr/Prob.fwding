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

#n=20:1:40
print('Input the type of grid  ')# and size m (101 or 121)')
lat_type =input("square(s) or triangular(t) ")
#m = float(input('m '))
m = 31
if lat_type == 's':
#Results of running prob_fwding_parallel.py on a grid with m=31 and delta = 0.1
	pkndelta_simu = [0.82,0.75,0.72,0.7,0.686,0.677,0.669,0.665,0.661,0.6552,0.6512,0.6462,0.6444,0.6402,0.638,0.636,0.6331,0.6303,0.6288,0.6277,0.6252] 
	tau_kndelta_simu = [15717.37, 14851.3, 14610.65, 14500.53, 14394.52, 14505.66, 14570.42, 14844.95, 14955.21, 14997.08, 14955.73, 15028.94, 15176.59, 15214.34, 15279.74, 15671.87, 15693.4, 15468.87, 15812.76, 16032.87, 15925.76]

#Results of running prob_fwding_parallel.py on a grid with m=31 and delta = 0.05
	pkndelta_simu1 = [0.84,0.77,0.74,0.715,0.7,0.69,0.681,0.6745,0.669,0.664,0.66,0.657,0.653,0.6504,0.6462,0.6442,0.641,0.6389,0.6366,0.6354,0.6323]
	tau_kndelta_simu1 = [16091.93, 15363.67, 15243.82, 15118.68, 15129.23, 15340.25, 15316.56, 15396.07, 15688.35, 15804.2, 15892.32, 16171.32, 16344.16, 16496.62, 16466.7, 16664.77, 16756.28, 16882.41, 16911.89, 17343.1, 17408.83]


if lat_type == 't':
#Results of running prob_fwding_parallel.py on a triangular grid with m=31 and delta = 0.1
	pkndelta_simu = [0.72,0.66,0.63,0.615,0.602,0.59,0.5835,0.5785,0.5735,0.5674,0.5634,0.5596,0.5562,0.5548,0.5518,0.5486,0.5458,0.5434,0.5414,0.5404,0.5387]
	tau_kndelta_simu = [13767.28, 13034.53, 12797.32, 12827.01, 12796.07, 12725.48, 12946.45, 13011.12, 13159.35, 13126.1, 13275.99, 13366.86, 13349.65, 13542.31, 13745.5, 13785.43, 13812.5, 13834.3, 14088.45, 14266.43, 14394.43]

#Results of running prob_fwding_parallel.py on a triangular grid with m=31 and delta = 0.05
	pkndelta_simu1 = [0.76,0.68,0.65,0.63,0.62,0.606,0.597,0.591,0.5845,0.5805,0.577,0.5724,0.5694,0.566,0.5622,0.5594,0.5576,0.5552,0.553,0.5496,0.5479]
	tau_kndelta_simu1 = [14585.1, 13554.56, 13430.86, 13341.87, 13632.07, 13514.09, 13643.96, 13800.97, 13976.97, 14204.11, 14325.39, 14441.08, 14737.82, 14866.61, 14837.34, 14926.73, 15238.91, 15348.77, 15456.62, 15482.77, 15603.12]

tau_kndelta_simu = [t/(m*m) for t in tau_kndelta_simu]
tau_kndelta_simu1 = [t/(m*m) for t in tau_kndelta_simu1]
#import from json file
with open("theta_thetaplus.json") as f:
	data = json.load(f)

# The lambda values in the file are from 1 to 4.99 in steps of 0.01
p = data["p"]
thetap = data["thetap"]
thetaplus = data["thetaplus"]

p_fine = np.arange(0.45,1,0.000001)
thetap_sq = [num**2 for num in thetap]
thetaplus_sq = [nump**2 for nump in thetaplus]
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
tau_kndelta_ergodic = thetaplus_pkndelta**2*np.arange(k,k+len(pkndelta_ergodic))*pkndelta_ergodic

#print(pkndelta_ergodic)
#print(tau_kndelta_ergodic)

dict={"m":m,"pkndelta_simu":pkndelta_simu,"pkndelta_simu1":pkndelta_simu1,"pkndelta_ergodic":list(pkndelta_ergodic),"tau_kndelta_simu":tau_kndelta_simu,"tau_kndelta_simu1":tau_kndelta_simu1,"tau_kndelta_ergodic":list(tau_kndelta_ergodic)}
json = json.dumps(dict)
f= open("simu_results.json","w")
f.write(json)
f.close()

