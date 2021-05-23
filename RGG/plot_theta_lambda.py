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

fig,ax = plt.subplots(1,1)
fig.set_size_inches(5, 2.3)
#fig.suptitle(r'For an RGG in a $251 \times 251$ area with connection radius $r=1$.')
#ax.plot(lbda,theta_lambda,"o",label='on 101 by 101 area')
#ax.plot(lbda,theta_lambda,"o",label='fixed number of nodes')
#ax.plot(lbda,theta_lambda_random,label='random number of nodes')
ax.plot(lbda,theta_lambda_251,label='Averaged over 100 realizations \n of $RGG(\lambda,1)$ generated on a \n 251 by 251 area')
#ax.set_title(r'Percolation probability ($\theta(\lambda)$)')
plt.xlabel(r'Intensity ($\lambda$)')
plt.legend(prop={'size': 10},loc='lower right')
plt.tight_layout()

plt.show()
