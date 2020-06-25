import matplotlib.pyplot as plt
import json

with open("theta_lambda.json") as f:
	data = json.load(f)

lbda = data["lambda"]
theta_lambda = data["theta_lambda"]
theta_lambda_random = data["theta_lambda_random"]

fig,ax = plt.subplots(1,1)
fig.suptitle('For an RGG in a 101 by 101 grid with connection radius =1.')
ax.plot(lbda,theta_lambda,"o",label='fixed number of nodes')
ax.plot(lbda,theta_lambda_random,label='random number of nodes')
ax.set_title('Percolation probability (\theta(lambda))')
plt.xlabel('Intensity (\lambda)')

plt.legend()
plt.show()
