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
k = 20
delta = 0.1
height = 12
#n=20:1:40
#Results of probabilistic forwarding for a doubletree of height 12 (root at height 0) with k=20 packets and n varying from 20 to 40
pkndelta = [0.987,0.97,0.9598,0.9493,0.9406,0.9329,0.9256,0.92,0.9135,0.9087,0.9039,0.8999,0.8955,0.8917,0.8878,0.8843,0.8813,0.8781,0.8755,0.8736,0.8692]
tau_kndelta = [241174.96, 243346.47, 247158.11, 248878.03, 249597.96, 249756.27, 248245.96, 253127.83, 251732.02, 251379.1, 252763.77, 253911.97, 253251.16, 253007.39, 252942.02, 254398.44, 256532.26, 257868.67, 254774.84, 260276.38, 255671.11]
dict={"height":height,"k":k,"pkndelta":pkndelta,"tau_kndelta":tau_kndelta}
json = json.dumps(dict)
f= open("doubletree_simu_results.json","w")
f.write(json)
f.close()
