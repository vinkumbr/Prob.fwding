# This file has the results for the simulations for RGGs with intensity 4.5, m = 101 and radius = 1.
# The adjacency matrices for these are stored in ./AdjMats/RGG4.5_average/

import matplotlib.pyplot as plt
import json

lbda = 4.5
k=20
m=101
# With the pkndelta values taken as the ones obtained for ./AdjMats/RGG_101_int_4.5.txt which is
pkndelta=[0.519,0.448,0.417,0.395,0.386,0.377,0.369,0.365,0.3605,0.357,0.355,0.35280,0.34980,0.34840,0.34720,0.3457,0.3438,0.34300,0.34210,0.3409,0.3401]
# Transmissions for filename = RGG_101_int_4.5.txt
tau_kndelta_simu=[473877.0, 421523.66, 404229.58, 385503.37, 389178.52, 384351.29, 383509.59, 387956.2, 383379.07, 390788.11, 394998.01, 397147.49, 393409.78, 402471.6, 404411.08, 409427.06, 409307.46, 409587.61, 422560.22, 419275.77, 416047.03]
# Transmissions for filename = RGG1_101_int_4.5.txt
trans1=[474760.01, 426097.49, 409143.15, 396805.09, 399593.06, 397941.74, 395877.44, 399568.68, 402198.35, 405218.59, 414530.8, 412624.44, 414156.87, 420139.39, 425698.21, 423709.8, 426009.19, 429359.8, 439549.21, 434627.32, 445107.67]
# Transmissions for filename = RGG2_101_int_4.5.txt
trans2=[473583.54, 416206.53, 396966.42, 375519.15, 372305.92, 367652.9, 354818.0, 359433.57, 361123.82, 355677.29, 363669.95, 362496.08, 356595.29, 357979.19, 368796.79, 362804.38, 360256.74, 371136.45, 367546.96, 360602.04, 367213.06]
# Transmissions for filename = RGG3_101_int_4.5.txt
trans3=[474914.51, 426161.29, 411212.37, 399214.81, 400087.0, 404060.31, 398929.63, 404733.87, 409843.16, 411517.32, 415526.92, 421958.34, 418926.04, 428877.27, 433318.03, 434669.21, 432257.35, 441344.24, 444076.94, 443068.29, 449465.46]
# Transmissions for filename = RGG4_101_int_4.5.txt
trans4=[474450.72, 424839.53, 406903.75, 395982.4, 397221.79, 397472.95, 393963.18, 400528.15, 401853.04, 404895.71, 406468.83, 413277.5, 413443.06, 417562.57, 421438.66, 427196.17, 423044.44, 433881.21, 435504.22, 432890.95, 441892.86]
# Transmissions for filename = RGG5_101_int_4.5.txt
trans5=[474583.25, 426216.11, 409746.33, 395681.94, 397980.21, 399232.58, 396231.23, 399170.4, 396866.71, 396814.06, 405478.18, 412514.73, 409286.09, 412861.04, 418511.49, 419785.58, 420615.05, 423863.12, 429492.65, 429842.9, 437756.58]
# Transmissions for filename = RGG6_101_int_4.5.txt
trans6=[474592.31, 422912.32, 405826.94, 389219.12, 385616.94, 378700.24, 371969.72, 375435.26, 366595.78, 367325.43, 370037.06, 372252.83, 368250.23, 364940.36, 374734.21, 373156.04, 370791.38, 369652.93, 375243.8, 374090.1, 374215.12]
# Transmissions for filename = RGG6_101_int_4.5.txt
trans7=[474799.21, 426347.95, 411094.16, 398598.1, 401371.75, 401061.62, 399195.26, 406144.89, 409338.56, 410977.72, 420638.64, 422227.96, 422394.69, 430664.15, 435936.31, 437054.24, 437769.17, 448623.96, 451908.78, 456502.7, 457005.95]
# Transmissions for filename = RGG6_101_int_4.5.txt
trans8=[474799.93, 424224.48, 407252.22, 393276.08, 395989.74, 394367.05, 390965.06, 394421.07, 395483.21, 398011.3, 405668.54, 408198.12, 406017.41, 413462.0, 419299.61, 422248.82, 424214.51, 428168.85, 436743.34, 435565.37, 436454.16]
# Transmissions for filename = RGG6_101_int_4.5.txt
trans9=[474356.42, 426057.27, 410395.41, 397540.18, 398889.64, 400217.72, 398167.58, 403702.33, 402610.79, 404669.2, 414222.13, 416249.49, 416093.81, 421832.81, 426402.2, 428520.01, 430525.47, 434428.08, 442129.87, 441026.43, 446187.28]
# Average number of transmissions
avg_trans = [tau_kndelta_simu[j]+trans1[j]+trans2[j]+trans3[j]+trans4[j]+trans5[j]+trans6[j]+trans7[j]+trans8[j]+trans9[j] for j in range(len(trans1))]
avg_trans = [avg_trans[i]/10 for i in range(len(avg_trans))]
n = range(20,41)


#Ergodic result
lbda_pkndelta = [lbda*p for p in pkndelta]

#import from json file
with open("theta_lambda.json") as f:
	data = json.load(f)

# The lambda values in the file are from 1 to 4.99 in steps of 0.01
theta_lambda = data["theta_lambda"]
theta_lambda_random = data["theta_lambda_random"]
theta_lbda_kndelta = [theta_lambda[int((round(l,2)-1)/0.01)] for l in lbda_pkndelta]
theta_lbda_kndelta_square = [i**2 for i in theta_lbda_kndelta]
tau_kndelta_ergodic = [(k+i)*m**2*lbda_pkndelta[i]*theta_lbda_kndelta_square[i] for i in range(len(lbda_pkndelta))]


fig,ax = plt.subplots(1,1)
fig.suptitle('For an RGG in a 101 by 101 grid with connection radius =1 and intensity 4.5 with k=20 packets and delta = 0.1. ')
ax.plot(n,tau_kndelta_simu,label='Trace 0')
ax.plot(n,trans1,label='Trace 1')
ax.plot(n,trans2,label='Trace 2')
ax.plot(n,trans3,label='Trace 3')
ax.plot(n,trans4,label='Trace 4')
ax.plot(n,trans5,label='Trace 5')
ax.plot(n,trans6,label='Trace 6')
ax.plot(n,trans7,label='Trace 7')
ax.plot(n,trans8,label='Trace 8')
ax.plot(n,trans9,label='Trace 9')
ax.plot(n,avg_trans,'o',label='Average')
ax.plot(n,tau_kndelta_ergodic,label='Ergodic')
ax.set_title('Number of coded packets')
plt.xlabel('Intensity (\lambda)')

plt.legend()
plt.show()
