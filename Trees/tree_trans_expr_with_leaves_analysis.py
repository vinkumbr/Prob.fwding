# This is a trial code to check few things
import matplotlib.pyplot as plt

H=20
kappa = 2*100**(1/(H-1))
f1 = lambda n,j:n**((j-1)/(H-1))
max_n = 1000
result=[]
for i in range(100,max_n):
	sum = 0
	for j in range(H+1):
		sum = sum+kappa**(H-j)*f1(i,j)
	result.append(sum)

min_index = result.index(min(result))
print(min_index)
fig,ax= plt.subplots(1,1)
ax.plot(range(100,max_n),result)
plt.show()
