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
m= 101
#n=20:1:40
print('Input lambda (4 or 4.5 or 4.54 or 4.9)')# and size m (101 or 121)')
lbda = float(input('lambda '))
#Results of running prob_fwding_parallel.py on a RGG with M given by RGG_101_int_4.0.txt with m=101, lambda=4 and radius=1 
#if lbda==4:
#pkndelta_simu1=[0.58,0.51,0.48,0.455,0.435,0.43,0.421,0.412,0.409,0.4065,0.401,0.3995,0.397,0.395,0.3932,0.3914,0.3897,0.3882,0.3871,0.386,0.385]
#tau_kndelta_simu1=[470324.43, 427097.13, 415147.2, 400075.68, 386824.4, 391737.14, 390003.04, 382557.14, 387107.94, 391857.39, 386676.69, 395442.31, 400199.37, 395390.78, 401700.81, 401303.26, 408852.44, 407818.13, 409295.91, 417863.68, 418793.93]

#Results of running prob_fwding_parallel_recs_avg.py on RGG with M given by ./AdjMats/RGG4.0_average/*.txt with m=101, lambda=4.0 and radius=1. 10 realizations of RGG and 20 prob forwarding on each.
pkndelta_simu1=[0.59,0.5,0.47,0.449,0.433,0.425,0.416,0.41,0.4075,0.402,0.3995,0.3969,0.3937,0.3918,0.3904,0.3884,0.3868,0.3851,0.3839,0.3826,0.3822]
tau_kndelta_simu1=[478990.015, 419242.93, 407728.75, 398227.315, 392166.625, 394842.43, 391770.825, 396573.62, 403369.715, 401625.93, 406643.26, 411019.7, 410251.58, 415397.785, 420461.515, 421192.575, 424319.635, 424102.805, 424304.94, 430471.46, 434995.09]
tau_kndelta_simu1=[t/(101*101) for t in tau_kndelta_simu1]

#Results of running prob_fwding_parallel.py on a RGG with M given by RGG_101_int_4.5.txt with m=101, lambda=4.5 and radius=1 
#if lbda == 4.5:
#	pkndelta_simu=[0.519,0.448,0.417,0.395,0.386,0.377,0.369,0.365,0.3605,0.357,0.355,0.35280,0.34980,0.34840,0.34720,0.3457,0.3438,0.34300,0.34210,0.3409,0.3401]
#	tau_kndelta_simu=[473877.0, 421523.66, 404229.58, 385503.37, 389178.52, 384351.29, 383509.59, 387956.2, 383379.07, 390788.11, 394998.01, 397147.49, 393409.78, 402471.6, 404411.08, 409427.06, 409307.46, 409587.61, 422560.22, 419275.77, 416047.03]

#Results of running prob_fwding_parallel_recs_avg.py on RGG with M given by ./AdjMats/RGG4.5_average/*.txt with m=101, lambda=4.5 and radius=1. 10 realizations of RGG and 20 prob forwarding on each.
if lbda == 4.5:
	pkndelta_simu = [0.498,0.434,0.408,0.395,0.382,0.374,0.368,0.364,0.3601,0.3572,0.3548,0.3522,0.3502,   0.3479,0.3465,0.346,0.3445,0.3437,0.3419,0.3413,0.3404]
	tau_kndelta_simu = [454096.61, 409689.815, 395773.97, 392819.375, 387389.275, 386460.125, 389011.835, 391003.62, 392094.54, 395676.51, 402518.52, 401771.14, 406296.3, 405092.09, 404213.2, 415875.355, 419580.805, 422831.875, 420917.8, 426195.71, 430323.0]


#Results of running prob_fwding_parallel.py on a RGG with M given by RGG_M.txt with m=101, lambda=4.54 and radius=1 
#if lbda == 4.54:
#	pkndelta_simu=[0.59,0.504,0.452,0.429,0.406,0.395,0.385,0.377,0.37,0.365,0.361,0.358,0.355,0.353,0.35,0.348,0.3464,0.3457,0.3439,0.342,0.341]
#	tau_kndelta_simu=[543226.33999999997, 481529.90999999997, 439355.02000000002, 422168.51000000001, 408202.78000000003, 405761.42999999999, 391214.03000000003, 392616.51000000001, 386506.12, 385633.88, 384712.65999999997, 388600.75, 396060.92999999999, 396466.79999999999, 397323.46999999997, 394216.03000000003, 400485.15999999997, 398709.42999999999, 403578.78999999998, 402104.57000000001, 403572.15999999997]

#Results of running prob_fwding_parallel.py on a RGG with M given by RGG_101_int_4.54.txt with m=101, lambda=4.54 and radius=1 
if lbda == 4.54:
	pkndelta_simu=[0.47,0.413,0.39,0.375,0.367,0.36,0.355,0.351,0.3484,0.3458,0.344,0.342,0.341,0.33870,0.33740,0.3364,0.33550,0.33440,0.33350,0.33290,0.3326]
	tau_kndelta_simu=[432041.71, 392702.59, 381188.66, 375174.29, 376823.36, 378748.26, 378833.7, 381055.53, 385753.76, 391771.69, 395544.74, 396400.75, 404589.14, 401521.97, 406248.87, 408725.19, 414391.83, 414023.38, 417468.58, 422969.66, 430931.63]

#Results of running prob_fwding_parallel.py on a RGG with M given by RGG_101_int_4.9.txt with m=101, lambda=4.9 and radius=1 
if lbda == 4.9:
	pkndelta_simu=[0.443,0.389,0.366,0.352,0.344,0.337,0.3332,0.3287,0.3256,0.3231,0.322,0.319,0.3175,0.3159,0.3151,0.3136,0.3128,0.3119,0.31080,0.3104,0.30940]
	tau_kndelta_simu=[439837.94, 398625.25, 387033.95, 379955.03, 380665.53, 379832.85, 385735.42, 386591.03, 389623.16, 395614.26, 403680.93, 397214.78, 404585.22, 407071.51, 415057.73, 418603.48, 423912.41, 426199.1, 423906.22, 434126.27, 433942.22]
tau_kndelta_simu = [i/101/101 for i in tau_kndelta_simu]


#if lbda == 4.5:
#Results of running prob_fwding_parallel.py on a RGG with M given by RGG_121_int_4.5.txt with m=121, lambda=4.5 and radius=1 
pkndelta_simu_big=[0.53,0.466,0.438,0.41,0.397,0.387,0.379,0.374,0.368,0.3625,0.359,0.357,0.354,0.352,0.35040,0.34850,0.34730,0.34600,0.34410,0.34330,0.34160]
tau_kndelta_simu_big=[694055.45, 630085.86, 605412.7, 578622.33, 561357.79, 562529.67, 554685.49, 560588.43, 557005.0, 547282.72, 547510.22, 569253.33, 563719.62, 565428.26, 569755.36, 572603.61, 574126.68, 580712.6, 581478.88, 594278.32, 577293.84]
tau_kndelta_simu_big=[i/121/121 for i in tau_kndelta_simu_big]

#Ergodic result
lbda_pkndelta = [lbda*p for p in pkndelta_simu]

#import from json file
with open("theta_lambda.json") as f:
	data = json.load(f)

# The lambda values in the file are from 1 to 4.99 in steps of 0.01
lamb = data["lambda"]
theta_lambda = data["theta_lambda"]
theta_lambda_251 = data["theta_lambda_251"]
theta_lambda_random = data["theta_lambda_random"]
theta_lbda_kndelta = [theta_lambda_251[int((round(m,2)-1)/0.01)] for m in lbda_pkndelta]
theta_lbda_kndelta_square = [i**2 for i in theta_lbda_kndelta]

#tau_kndelta_ergodic = [(k+i)*lbda_pkndelta[i]*theta_lbda_kndelta_square[i] for i in range(len(lbda_pkndelta))]

p = np.arange(0.3,0.65,0.0000001)
lbda_p = lbda*p
f = interp1d(lamb,theta_lambda_251)
theta_lbda_p = f(lbda_p)
theta_lbda_p_square = theta_lbda_p*theta_lbda_p
theta_plus = theta_lbda_p 
index = 0
print(k)
pkndelta_ergodic = np.zeros(k+1)
n=k
while n<=40:
	minp_index = 0
	prob_cdf = np.zeros(len(p))
	prob_sum = np.zeros(len(p))
	for j in range(k):
		prob_sum = binomial(n,j)*theta_lbda_p_square**j*(1-theta_lbda_p_square)**(n-j)
		prob_cdf = prob_cdf+prob_sum
	prob = lbda*(binom.cdf(k-1,n,theta_lbda_p**2))
	try:
		minp_index = min(np.where(prob_cdf<=delta)[0])
	except:
		minp_index = -1
	pkndelta_ergodic[index] = p[minp_index]
	#print(minp_index) 
	index = index+1
	n=n+1
print(pkndelta_ergodic)
prob_from_simu = np.array(pkndelta_simu)
thetaplus_pfs = f(lbda*prob_from_simu)
tau_kndelta_pfs = lbda*prob_from_simu*thetaplus_pfs**2*np.arange(k,k+len(prob_from_simu))
thetaplus_lambdap = f(lbda*pkndelta_ergodic)
tau_kndelta_ergodic = lbda*pkndelta_ergodic*thetaplus_lambdap**2*np.arange(k,k+len(pkndelta_ergodic))

#print(pkndelta_ergodic)
#print(tau_kndelta_ergodic)

dict={"lbda":lbda,"pkndelta_simu":pkndelta_simu,"pkndelta_simu1":pkndelta_simu1,"pkndelta_ergodic":list(pkndelta_ergodic),"prob_from_simu":list(prob_from_simu),"pkndelta_simu_big":pkndelta_simu_big,"tau_kndelta_simu":tau_kndelta_simu,"tau_kndelta_simu1":tau_kndelta_simu1,"tau_kndelta_pfs":list(tau_kndelta_pfs),"tau_kndelta_simu_big":tau_kndelta_simu_big,"tau_kndelta_ergodic":list(tau_kndelta_ergodic)}
json = json.dumps(dict)
f= open("simu_results.json","w")
f.write(json)
f.close()

