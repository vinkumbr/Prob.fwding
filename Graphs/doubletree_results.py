import json
import numpy as np

# From simulations
delta = 0.1
height = input('Enter the height')
#n=20:1:40


#Results of probabilistic forwarding for a doubletree of height 12 (root at height 0) with k=20 packets and n varying from 20 to 40
if height == 12:
	k=20
	pkndelta = [0.987,0.97,0.9598,0.9493,0.9406,0.9329,0.9256,0.92,0.9135,0.9087,0.9039,0.8999,0.8955,0.8917,0.8878,0.8843,0.8813,0.8781,0.8755,0.8736,0.8692]
	tau_kndelta = [241174.96, 243346.47, 247158.11, 248878.03, 249597.96, 249756.27, 248245.96, 253127.83, 251732.02, 251379.1, 252763.77, 253911.97, 253251.16, 253007.39, 252942.02, 254398.44, 256532.26, 257868.67, 254774.84, 260276.38, 255671.11]

#Results of probabilistic forwarding for a doubletree of height 9 (root at height 0) with k=100 packets and n varying from 100 to 200 in steps of 10
if height == 9:
	k = 100
	pkndelta=[0.993,0.945,0.922,0.903,0.89,0.877,0.868,0.859,0.851,0.844,0.838]
	tau_kndelta=[152174.96, 149333.27, 149265.44, 147667.93, 147660.74, 146104.94, 146780.41, 146331.05, 145775.39, 146157.11, 146216.09]

dict={"height":height,"k":k,"pkndelta":pkndelta,"tau_kndelta":tau_kndelta}
json = json.dumps(dict)
f= open("doubletree_simu_results.json","w")
f.write(json)
f.close()
