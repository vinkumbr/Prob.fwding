
import json
import numpy as np

H = 10
k = input("Enter the value of k (20 or 100)")
if k =='100':
	n = np.arange(100,201,10)
	#Probabilistic forwarding on a binary tree of height H=10 (1024 leaf nodes) with k=100 and n=100:10:200 with delta =0.1
	pkndelta_1=[0.9999, 0.9919, 0.9835, 0.9757, 0.9679, 0.9608, 0.9542, 0.9482, 0.9424, 0.9369, 0.9315]
	taukndelta_1=[204506.48, 209177.07, 211429.47, 213010.18, 214001.59, 213956.05, 215258.03, 215581.07, 216675.23, 216984.35, 217415.25]

	#Probabilistic forwarding on a binary tree of height H=10 (1024 leaf nodes) with k=100 and n=100:10:200 with delta =0.05
	pkndelta_05=[0.9999,0.9932,0.985,0.9772,0.9702,0.9636,0.9569,0.9508,0.9451,0.9397,0.9348]
	taukndelta_05=[204530.67, 211806.74, 214491.55, 216355.69, 218549.57, 220622.01, 220214.13, 221814.46, 221966.78, 223775.35, 225011.67]

if k=='20':
	n = np.arange(20,41,1)
	#Probabilistic forwarding on a binary tree of height H=10 (1024 leaf nodes) with k=20 and n=20:1:40 with delta =0.1
	pkndelta_1=[0.9993,0.9969,0.9936,0.9905,0.9868,0.9834,0.9799,0.976,0.9732,0.9698,0.966,0.9634,0.9606,0.9576,0.955,0.952,0.95,0.9467,0.9439,0.9418,0.9393]
	taukndelta_1=[40685.91, 41751.03, 42563.31, 43151.44, 43722.16, 44002.89, 44248.48, 44598.7, 44944.52, 44839.09, 45066.01, 45511.17, 45647.35, 45723.86, 45856.65, 45739.09, 46564.64, 46270.73, 46359.42, 46529.92, 47202.63]

	#Probabilistic forwarding on a binary tree of height H=10 (1024 leaf nodes) with k=20 and n=20:1:40 with delta =0.05
	pkndelta_05=[0.9997,0.9979,0.9952,0.9922,0.9893,0.9863,0.9831,0.98,0.9765,0.974,0.9709,0.9677,0.9652,0.9622,0.9597,0.9575,0.9549,0.9521,0.9498,0.9474,0.945]
	taukndelta_05=[40799.61, 42279.58, 43178.38, 43888.99, 44623.07, 45019.77, 45419.59, 46012.7, 46297.27, 47226.88, 47117.96, 47740.64, 47625.27, 47807.55, 48052.92, 48344.74, 48592.63, 48576.7, 49185.21, 49030.69, 49404.19]


dict={'height':H,'n':n.tolist(),'pkndelta_1':pkndelta_1,'taukndelta_1':taukndelta_1,'pkndelta_05':pkndelta_05,'taukndelta_05':taukndelta_05}
json = json.dumps(dict)
f= open("bintree_simu_results.json","w")
f.write(json)
f.close()

