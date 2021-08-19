import matplotlib.pyplot as plt
import json
import math

e = math.e
with open("theta_thetaplus.json") as f:
	data = json.load(f)

p = data["p"]
thetap = data["thetap"]
thetapext = [thetap[i]/p[i] for i in range(len(p))]
print(len(p),len(thetap))

fig,ax = plt.subplots(1,1)
fig.set_size_inches(5, 2.5)
ax.plot(p,thetap,'--',label='$\\theta(p)$')
ax.plot(p,thetapext,label='$\\theta^{ext}(p)$')
#ax.set_title(r'Percolation probability')
plt.xlabel(r'p')
#plt.legend(prop={'size': 10},loc='lower right')
plt.legend(prop={'size': 10})
plt.tight_layout()

plt.show()
