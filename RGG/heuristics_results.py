import json
import numpy as np
from scipy.interpolate import interp1d
from scipy.stats import binom
import datetime

def binomial(n, k):
    if not 0 <= k <= n:
        return 0
    b = 1
    for t in range(min(k, n-k)):
        b *= n
        b //= t+1
        n -= 1
    return b

k=20
delta=0.1
m= 101
#n=20:1:40
lbda = 4

pkndelta_simu= [0.55,0.49,0.46,0.438,0.426,0.4195,0.4116,0.406,0.402,0.399,0.3958,0.3936,0.3919,
0.3898,0.38830,0.3864,0.385,0.3839,0.3829,0.3819,0.38100]
tau_kndelta_simu=[445910.16, 411001.01, 397756.945, 386174.745, 381840.235, 388367.705, 387463.145, 387430.885, 391329.725, 392842.31, 396894.535, 402186.86, 404928.765, 408568.56, 415804.82, 413514.12, 417665.23, 421950.91, 428217.495, 428126.895, 432020.37]
tau_kndelta_simu=[t/(lbda*101*101) for t in tau_kndelta_simu]

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

p = np.arange(0.3,0.65,0.0000001)
lbda_p = lbda*p
f = interp1d(lamb,theta_lambda_251)
theta_lbda_p = f(lbda_p)
theta_lbda_p_square = theta_lbda_p*theta_lbda_p
theta_plus = theta_lbda_p 
theta_denom = f(lbda)
print(theta_denom)
delta_prime = 1-theta_denom*(1-delta)
print(delta_prime)
index = 0
print(k)
pkndelta_ergodic = np.zeros(k+1)
n=k
while n<=40:
	print(n)
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
pkndelta_ergodic = pkndelta_ergodic / theta_denom

thetaplus_lambdap = f(lbda*pkndelta_ergodic)
tau_kndelta_ergodic = pkndelta_ergodic*thetaplus_lambdap**2*np.arange(k,k+len(pkndelta_ergodic))

time = datetime.datetime.now
dict = {'time':str(time),'lbda':4,'m':101,'k':20,'pkndelta_simu':pkndelta_simu,'tau_kndelta_simu':tau_kndelta_simu,'pkndlta_heur':list(pkndelta_ergodic),'tau_kndelta_heur':list(tau_kndelta_ergodic)}
json = json.dumps(dict,indent=2)
f= open("heur_results.json","w")
f.write(json)
f.close()