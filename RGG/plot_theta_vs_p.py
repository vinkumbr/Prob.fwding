import matplotlib.pyplot as plt
import json
import numpy as np
from scipy.interpolate import interp1d

#import from json file
with open("theta_lambda.json") as f:
	data = json.load(f)

# The lambda values in the file are from 1 to 4.99 in steps of 0.01
lamb = data["lambda"]
theta_lambda = data["theta_lambda"]
theta_lambda_251 = data["theta_lambda_251"]
theta_lambda_random = data["theta_lambda_random"]
#for lambda = 4.5
pkndelta = [0.498,0.434,0.408,0.395,0.382,0.374,0.368,0.364,0.3601,0.3572,0.3548,0.3522,0.3502,   0.3479,0.3465,0.346,0.3445,0.3437,0.3419,0.3413,0.3404]
#for lambda = 4
#pkndelta = [0.59,0.5,0.47,0.449,0.433,0.425,0.416,0.41,0.4075,0.402,0.3995,0.3969,0.3937,0.3918,0.3904,0.3884,0.3868,0.3851,0.3839,0.3826,0.3822]
ini_lamb = [0.01*i for i in range(100)]
lamb = ini_lamb+lamb
ini_theta = [0 for i in range(len(ini_lamb))]
theta_lambda_251 = ini_theta+theta_lambda_251
#print(theta_lambda_251)
p = np.arange(0,1,0.0001)
lbda1 = 4.5
lbda1_p = lbda1*p
lbda2 = 4
lbda2_p = lbda2*p
f = interp1d(lamb,theta_lambda_251)
theta_lbda1_p = f(lbda1_p)
theta_lbda2_p = f(lbda2_p)

fig1,ax1 = plt.subplots(1,1)
fig1.set_size_inches(5, 2.5)
fig1.suptitle('Intensity $\lambda=4.5$')
#ax1.plot(p,theta_lbda1_p,'o-',label='$\lambda=4.5$')
ax1.plot(p,theta_lbda1_p,'s-',label=r'$\theta (\lambda p)$')
ax1.plot(p,p,label='$p$')
ax1.plot(pkndelta,pkndelta,'+',label='simulations ($\lambda=4.5$)')
plt.xlabel('Forwarding probability (p)')
plt.tight_layout()
ax1.legend()
plt.show()

