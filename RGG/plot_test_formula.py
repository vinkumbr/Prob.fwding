import json
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

lbda = 4.5
m=101
# Results of the trans_from_p_test_formula for n=1 pkt with p values as below
#pkndelta=[0.4,0.5,0.6,0.7,0.8,0.9]
#trans_from_simu = [17462.9326,22795.9835, 27509.5575, 32125.0597, 36721.5718, 41312.6943]

#pkndelta=[0.33,0.34,0.35,0.36,0.37,0.38,0.39,0.4,0.41,0.42,0.43,0.44,0.45,0.46,0.47,0.48,0.49,0.5,0.6,0.7,0.8,0.9]
#trans_from_simu = [ 8291.213,  10936.0183, 12920.1632, 14182.1264, 15172.5103, 16014.7767,16759.6235,17464.9413, 18103.1911, 18618.6264, 19236.1485,19755.0609,20306.1788, 20807.0342, 21296.5837, 21814.6539, 22313.3708, 22817.1542,27509.5575, 32125.0597, 36721.5718, 41312.6943]

pkndelta = np.arange(0.34,0.361,0.001)
pkndelta = list(pkndelta)
#trans_from_simu = [ 8291.213,  8622.3873,  8865.2299,  9158.9303,  9452.261,   9727.877,  9960.1239, 10243.9035, 10574.599,  10675.5662, 10950.1165, 11138.0649, 11393.1084, 11569.2891, 11783.7064, 12060.5172, 12184.5987, 12333.5975, 12487.0412, 12665.7534, 12814.0932, 13031.8681, 13086.6304, 13324.7888, 13413.7331, 13536.3817, 13716.9711, 13816.2633, 13963.9989, 14091.2857, 14151.2738]
trans_from_simu = [10950.1165, 11138.0649, 11393.1084, 11569.2891, 11783.7064, 12060.5172, 12184.5987, 12333.5975, 12487.0412, 12665.7534, 12814.0932, 13031.8681, 13086.6304, 13324.7888, 13413.7331, 13536.3817, 13716.9711, 13816.2633, 13963.9989, 14091.2857, 14151.2738]
#Ergodic result
lbda_pkndelta = [lbda*p for p in pkndelta]

#import from json file
with open("theta_lambda.json") as f:
	data = json.load(f)

# The lambda values in the file are from 1 to 4.99 in steps of 0.01
lamb = data["lambda"]
theta_lambda = data["theta_lambda"]
theta_lambda_251 = data["theta_lambda_251"]
theta_lambda_random = data["theta_lambda_random"]
f = interp1d(lamb,theta_lambda_251)
theta_lbda_kndelta = f(lbda_pkndelta)
#theta_lbda_kndelta = [theta_lambda_251[int((round(k,2)-1)/0.01)] for k in lbda_pkndelta]
theta_lbda_kndelta_square = [i**2 for i in theta_lbda_kndelta]

tau_kndelta_ergodic = [m**2*lbda_pkndelta[i]*theta_lbda_kndelta_square[i] for i in range(len(lbda_pkndelta))]

fig,ax = plt.subplots(1,1)
fig.suptitle('For an RGG in a 101 by 101 grid with connection radius =1 and intensity 4.5.')
ax.plot(pkndelta,tau_kndelta_ergodic,"o",label='from ergodicity')
ax.plot(pkndelta,trans_from_simu,label='from simulations')
ax.set_title('Expected cluster size of the origin (averaged over 100 realizations of the RGG and 100 thinnings for each graph)')
plt.xlabel('Forwarding probability (p)')

plt.legend()
plt.show()
