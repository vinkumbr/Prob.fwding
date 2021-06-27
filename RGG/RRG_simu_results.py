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
nodes = 1000
# Results of the probabilistic forwarding protocol on a random 4-regular graph of 1000 nodes with n varying from 20 to 40 on the realizations present in ./AdjMats/RRG/*.txt
d = 4
pkndelta_simu = [0.8,0.7,0.64,0.61,0.588,0.564,0.55,0.54,0.53,0.518,0.5095,0.5038,0.4982,0.4918,0.4854,0.4808, 0.4759,0.4725,0.4691,0.4651,0.4616]
tau_kndelta_simu = [15950.185, 14384.09, 13372.57, 13005.1, 12648.23, 12242.855, 12067.52, 12099.325, 11934.42, 11644.085, 11507.6, 11605.995, 11625.68, 11365.935, 11219.5, 11290.62, 11037.965, 10964.985, 11197.705, 11030.25, 11014.365]


# Results of the probabilistic forwarding protocol on a random 8-regular graph of 1000 nodes with n varying from 20 to 40 on the realizations present in ./AdjMats/RRG/*.txt
d1 = 8
pkndelta_simu1 = [0.55,0.43,0.39,0.355,0.333,0.317,0.3035,0.2935,0.285,0.278,0.272,0.265, 0.26,0.254,0.2508,0.2474,0.2444,0.2413,0.2379,0.2352,0.2333]
tau_kndelta_simu1 = [10979.485, 8844.385, 8201.255, 7596.335, 7208.085, 6891.99, 6714.475, 6535.525, 6409.92, 6341.995, 6257.55, 6062.01, 5958.975, 5837.74, 5890.975, 5868.595, 5796.71, 5682.225, 5665.78, 5543.295, 5578.53]

dict={"d":d,"d1":d1,"nodes":nodes,"pkndelta_simu":pkndelta_simu,"pkndelta_simu1":pkndelta_simu1, "tau_kndelta_simu":tau_kndelta_simu,"tau_kndelta_simu1":tau_kndelta_simu1}
json = json.dumps(dict)
f= open("RRG_simu_results.json","w")
f.write(json)
f.close()
