import matplotlib.pyplot as plt
import json
import math

e = math.e
with open("theta_lambda.json") as f:
	data = json.load(f)

lbda = data["lambda"]
theta_lambda = data["theta_lambda"]
theta_lambda_random = data["theta_lambda_random"]
theta_lambda_251 = data["theta_lambda_251"]

bool_IOC = [1-e**(-l*math.pi) for l in lbda]

fig,ax = plt.subplots(1,1)
fig.suptitle('For an RGG in a 101 by 101 grid with connection radius =1.')
ax.plot(lbda,theta_lambda,"o",label='on 101 by 101 area')
#ax.plot(lbda,theta_lambda,"o",label='fixed number of nodes')
#ax.plot(lbda,theta_lambda_random,label='random number of nodes')
ax.plot(lbda,bool_IOC,"+",label='BM-IOC')
ax.plot(lbda,theta_lambda_251,label='on 251 by 251 area')
ax.set_title('Percolation probability (\theta(lambda))')
plt.xlabel('Intensity (\lambda)')

plt.legend()
plt.show()
