import json

# From simulations
k=20
delta=0.1
m= 101
#n=20:1:40

#Results of running prob_fwding_parallel.py on a RGG with M given by RGG_101_int_4.0.txt with m=101, lambda=4 and radius=1 
#lbda=4
#pkndelta_simu=[0.58,0.51,0.48,0.455,0.435,0.43,0.421,0.412,0.409,0.4065,0.401,0.3995,0.397,0.395,0.3932,0.3914,0.3897,0.3882,0.3871,0.386,0.385]
#tau_kndelta_simu=[470324.43, 427097.13, 415147.2, 400075.68, 386824.4, 391737.14, 390003.04, 382557.14, 387107.94, 391857.39, 386676.69, 395442.31, 400199.37, 395390.78, 401700.81, 401303.26, 408852.44, 407818.13, 409295.91, 417863.68, 418793.93]

#Results of running prob_fwding_parallel.py on a RGG with M given by RGG_M.txt with m=101, lambda=4.54 and radius=1 
lbda=4.54
pkndelta_simu=[0.59,0.504,0.452,0.429,0.406,0.395,0.385,0.377,0.37,0.365,0.361,0.358,0.355,0.353,0.35,0.348,0.3464,0.3457,0.3439,0.342,0.341]
tau_kndelta_simu=[543226.33999999997, 481529.90999999997, 439355.02000000002, 422168.51000000001, 408202.78000000003, 405761.42999999999, 391214.03000000003, 392616.51000000001, 386506.12, 385633.88, 384712.65999999997, 388600.75, 396060.92999999999, 396466.79999999999, 397323.46999999997, 394216.03000000003, 400485.15999999997, 398709.42999999999, 403578.78999999998, 402104.57000000001, 403572.15999999997]

#Results of running prob_fwding_parallel.py on a RGG with M given by RGG_101_int_4.9.txt with m=101, lambda=4.9 and radius=1 
#lbda=4.9
pkndelta_simu=[0.443,0.389,0.366,0.352,0.344,0.337,0.3332,0.3287,0.3256,0.3231,0.322,0.319,0.3175,0.3159,0.3151,0.3136,0.3128,0.3119,0.31080,0.3104,0.30940]
tau_kndelta_simu=[439837.94, 398625.25, 387033.95, 379955.03, 380665.53, 379832.85, 385735.42, 386591.03, 389623.16, 395614.26, 403680.93, 397214.78, 404585.22, 407071.51, 415057.73, 418603.48, 423912.41, 426199.1, 423906.22, 434126.27, 433942.22]

#Ergodic result
lbda_pkndelta = [lbda*p for p in pkndelta_simu]

#import from json file
with open("theta_lambda.json") as f:
	data = json.load(f)

# The lambda values in the file are from 1 to 4.99 in steps of 0.01
theta = data["theta_lambda"]
theta_lambda_random = data["theta_lambda_random"]
theta_lbda_kndelta = [theta_lambda_random[int((round(k,2)-1)/0.01)] for k in lbda_pkndelta]
theta_lbda_kndelta_square = [i**2 for i in theta_lbda_kndelta]

tau_kndelta_ergodic = [(k+i)*m**2*lbda_pkndelta[i]*theta_lbda_kndelta_square[i] for i in range(len(lbda_pkndelta))]

dict={"pkndelta_simu":pkndelta_simu,"tau_kndelta_simu":tau_kndelta_simu,"tau_kndelta_ergodic":tau_kndelta_ergodic}
json = json.dumps(dict)
f= open("simu_results.json","w")
f.write(json)
f.close()

