import json
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

lbda = 4.5
m=101
p = np.arange(0.33,0.5,0.005)
q = 1-p
lbda_p = lbda*p
lbda_q = lbda*q

recs_from_simu = [23705.895833333332, 28379.354166666668, 33018.385416666664, 34548.864583333336, 36926.052083333336, 37001.166666666664, 41204.697916666664, 40455.135416666664, 40937.65625, 40912.770833333336, 42197.583333333336, 42033.520833333336, 43111.260416666664, 42969.875, 44421.260416666664, 44109.458333333336, 43325.84375, 44862.635416666664, 44015.09375, 44544.166666666664, 44661.427083333336, 44734.041666666664, 44402.34375, 44819.708333333336, 45322.59375, 45404.083333333336, 45415.0, 45071.46875, 45049.75, 45560.041666666664, 45602.46875, 44643.447916666664, 45151.479166666664, 45659.5]


#import from json file
with open("theta_lambda.json") as f:
	data = json.load(f)

# The lambda values in the file are from 1 to 4.99 in steps of 0.01
lamb = data["lambda"]
theta_lambda = data["theta_lambda"]
theta_lambda_251 = data["theta_lambda_251"]
theta_lambda_random = data["theta_lambda_random"]
f = interp1d(lamb,theta_lambda_251)
theta_lbda_p = f(lbda_p)
#theta_lbda_kndelta = [theta_lambda_251[int((round(k,2)-1)/0.01)] for k in lbda_pkndelta]
theta_lbda_p_square = [i**2 for i in theta_lbda_p]

recs_ergodic = [m**2*lbda_p[i]*theta_lbda_p_square[i]+m**2*lbda_q[i]*theta_lbda_p[i] for i in range(len(lbda_p))]

#another approx using theta^+ idea

thetaplus = theta_lbda_p/p
recs_plus_approx = [m**2*lbda_p[i]*thetaplus[i] for i in range(len(lbda_p))]


fig,ax = plt.subplots(1,1)
fig.suptitle('For an RGG in a 101 by 101 grid with connection radius =1 and intensity 4.5.')
ax.plot(p,recs_ergodic,"o",label='from ergodicity')
ax.plot(p,recs_from_simu,label='from simulations')
ax.plot(p,recs_plus_approx,"--",label='from theta^+')
ax.set_title('Expected cluster size of the origin (averaged over 100 realizations of the RGG and 100 thinnings for each graph)')
plt.xlabel('Forwarding probability (p)')

plt.legend()
plt.show()
