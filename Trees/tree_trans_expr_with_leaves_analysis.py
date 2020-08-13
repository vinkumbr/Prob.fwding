# This is a trial code to check few things
import matplotlib.pyplot as plt
import numpy as np


def trans_from_prob(prob,n):
	if len(prob) == len(n):
		trans = [n[i]*((2*prob[i])**(H+1)-1)/(2*prob[i]-1) for i in range(len(n))]
	else:
		print("Wrong length arrays")
		trans = None
	return trans

pkndelta_1=[0.9999, 0.9919, 0.9835, 0.9757, 0.9679, 0.9608, 0.9542, 0.9482, 0.9424, 0.9369, 0.9315]
taukndelta_1=[204506.48, 209177.07, 211429.47, 213010.18, 214001.59, 213956.05, 215258.03, 215581.07, 216675.23, 216984.35, 217415.25]
H=10
min_n = 100
max_n = 201
kappa = 2*min_n**(1/(H-1))
f1 = lambda n,j:n**((j-1)/(H-1))
pkndelta = []
tau_from_pkndelta_1=[]
result=[]
for i in range(min_n,max_n):
	sum = 0
	for j in range(H+1):
		sum = sum+kappa**(H-j)*f1(i,j)
	result.append(sum)

for i in range(len(pkndelta_1)):
	n = min_n+10*i
	p = pkndelta_1[i]
	pkndelta.append(1.005*(min_n/n)**(1/(H-1)))
	tau_from_pkndelta_1.append(n*((2*p)**(H+1)-1)/(2*p-1))

narray = np.arange(100,210,10)
tau_from_pkndelta = trans_from_prob(pkndelta,narray)

min_index = result.index(min(result))
print(min_index)
fig1,ax1= plt.subplots(1,1)
ax1.plot(range(min_n,max_n),result)
ax1.plot(narray,taukndelta_1,'--')
#ax1.plot(narray,tau_from_pkndelta_1,'o')
ax1.plot(narray,tau_from_pkndelta,'o')

fig2,ax2= plt.subplots(1,1)
ax2.plot(narray,pkndelta)
ax2.plot(narray,pkndelta_1,'--')
plt.show()
