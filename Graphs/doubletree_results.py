import json
import numpy as np

# From simulations
delta = 0.1
height = int(input('Enter the height'))
k = int(input('Enter k'))
#n=20:1:40


if height == 12:
#Results of probabilistic forwarding for a doubletree of height 12 (root at height 0) with k=100 packets and n varying from 100 to 200 in steps of 10
	if k == 100:
		pkndelta = [0.995,0.954,0.934,0.918,0.906,0.8955,0.887,0.8795,0.873,0.8675,0.861]
		tau_kndelta = [1221655.76, 1208536.66, 1209347.85, 1196064.19, 1195442.05, 1188552.64, 1191748.6, 1184049.21, 1191350.72, 1198166.03, 1184299.69]

#Results of probabilistic forwarding for a doubletree of height 12 (root at height 0) with k=20 packets and n varying from 20 to 40
	if k == 20:
		pkndelta = [0.987,0.97,0.9598,0.9493,0.9406,0.9329,0.9256,0.92,0.9135,0.9087,0.9039,0.8999,0.8955,0.8917,0.8878,0.8843,0.8813,0.8781,0.8755,0.8736,0.8692]
		tau_kndelta = [241174.96, 243346.47, 247158.11, 248878.03, 249597.96, 249756.27, 248245.96, 253127.83, 251732.02, 251379.1, 252763.77, 253911.97, 253251.16, 253007.39, 252942.02, 254398.44, 256532.26, 257868.67, 254774.84, 260276.38, 255671.11]

#Results of probabilistic forwarding for a doubletree of height 9 (root at height 0) with k=100 packets and n varying from 100 to 200 in steps of 10
if height == 9:
	if k == 100:
		pkndelta=[0.993,0.945,0.922,0.903,0.89,0.877,0.868,0.859,0.851,0.844,0.838]
		tau_kndelta=[152174.96, 149333.27, 149265.44, 147667.93, 147660.74, 146104.94, 146780.41, 146331.05, 145775.39, 146157.11, 146216.09]

#Results of probabilistic forwarding for a doubletree of height 9 (root at height 0) with k=20 packets and n varying from 20 to 40 in steps of 1
	if k == 20:
		pkndelta = [0.986,0.966,0.952,0.941,0.928,0.9195,0.912,0.9045,0.8995,0.894,0.8865,0.882,0.878,0.8725,0.8695,0.8636,0.8598,0.8562,0.8528,0.8498,0.8468]
		tau_kndelta=[30103.94, 30370.69, 30592.79, 30737.46, 30772.58, 30626.07, 30855.66, 30914.05, 31204.3, 31375.37, 30999.86, 31113.62, 31543.72, 31461.18, 31637.31, 31349.46, 31033.15, 31346.77, 31142.74, 31551.23, 31559.07]

dict={"height":height,"k":str(k),"pkndelta":pkndelta,"tau_kndelta":tau_kndelta}
json = json.dumps(dict)
f= open("doubletree_simu_results.json","w")
f.write(json)
f.close()
