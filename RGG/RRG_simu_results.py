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

# Results of the probabilistic forwarding protocol on a random 4-regular graph of 1000 nodes with n varying from 20 to 40 on the realizations present in ./AdjMats/RRG/*.txt
pkndelta_simu = [0.8,0.7,0.64,0.61,0.588,0.564,0.55,0.53,0.518,0.509,0.5038,0.4982,0.4918,0.4854,0.4808, 0.4759,0.4728,0.4691,0.4651,0.4616]
tau_kndelta_simu = [15952.665, 14389.455, 13339.19, 13013.195, 12726.205, 12210.835, 12061.255, 11450.69, 11175.085, 11132.985, 11189.81, 11184.11, 10995.635, 10806.085, 10840.305, 10858.755, 10896.04, 10796.17, 10671.285, 10769.13]



dict={"lbda":lbda,"pkndelta_simu":pkndelta_simu,"pkndelta_simu1":pkndelta_simu1,"pkndelta_ergodic":list(pkndelta_ergodic),"prob_from_simu":list(prob_from_simu),"pkndelta_simu_big":pkndelta_simu_big,"tau_kndelta_simu":tau_kndelta_simu,"tau_kndelta_simu1":tau_kndelta_simu1,"tau_kndelta_pfs":list(tau_kndelta_pfs),"tau_kndelta_simu_big":tau_kndelta_simu_big,"tau_kndelta_ergodic":list(tau_kndelta_ergodic)}
json = json.dumps(dict)
f= open("RRG_simu_results.json","w")
f.write(json)
f.close()
