#Results of running prob_fwding_parallel.py on a RGG with M given by RGG_M.txt with m=101, lambda=4.54 and radius=1 
#k=20
#delta=0.1
#n=20:1:40

import json
# From simulations
pkndelta_simu=[0.59,0.504,0.452,0.429,0.406,0.395,0.385,0.377,0.37,0.365,0.361,0.358,0.355,0.353,0.35,0.348,0.3464,0.3457,0.3439,0.342,0.341]

tau_kndelta_simu=[543226.33999999997, 481529.90999999997, 439355.02000000002, 422168.51000000001, 408202.78000000003, 405761.42999999999, 391214.03000000003, 392616.51000000001, 386506.12, 385633.88, 384712.65999999997, 388600.75, 396060.92999999999, 396466.79999999999, 397323.46999999997, 394216.03000000003, 400485.15999999997, 398709.42999999999, 403578.78999999998, 402104.57000000001, 403572.15999999997]

#Ergodic result
k=20
m= 101
lbda=4.54
lbda_pkndelta = [lbda*p for p in pkndelta_simu]

#import from json file
with open("theta_lambda.json") as f:
	data = json.load(f)

# The lambda values in the file are from 1 to 4.99 in steps of 0.01
theta = data["theta_lambda"]
theta_lbda_kndelta = [theta[int((round(k,2)-1)/0.01)] for k in lbda_pkndelta]
theta_lbda_kndelta_square = [i**2 for i in theta_lbda_kndelta]

tau_kndelta_ergodic = [(k+i)*m**2*lbda_pkndelta[i]*theta_lbda_kndelta_square[i] for i in range(len(lbda_pkndelta))]

dict={"pkndelta_simu":pkndelta_simu,"tau_kndelta_simu":tau_kndelta_simu,"tau_kndelta_ergodic":tau_kndelta_ergodic}
json = json.dumps(dict)
f= open("simu_results.json","w")
f.write(json)
f.close()

