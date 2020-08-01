
import json
import numpy as np

n = np.arange(100,201,10)
H = 10
#Probabilistic forwarding on a binary tree of height H=10 (1024 leaf nodes) with k=100 and n=100:10:200 with delta =0.1
pkndelta_1=[0.9999, 0.9919, 0.9835, 0.9757, 0.9679, 0.9608, 0.9542, 0.9482, 0.9424, 0.9369, 0.9315]
taukndelta_1=[204506.48, 209177.07, 211429.47, 213010.18, 214001.59, 213956.05, 215258.03, 215581.07, 216675.23, 216984.35, 217415.25]

#Probabilistic forwarding on a binary tree of height H=10 (1024 leaf nodes) with k=100 and n=100:10:200 with delta =0.05
pkndelta_05=[0.9999,0.9932,0.985,0.9772,0.9702,0.9636,0.9569,0.9508,0.9451,0.9397,0.9348]
taukndelta_05=[204530.67, 211806.74, 214491.55, 216355.69, 218549.57, 220622.01, 220214.13, 221814.46, 221966.78, 223775.35, 225011.67]

dict={'height':H,'n':n.tolist(),'pkndelta_1':pkndelta_1,'taukndelta_1':taukndelta_1,'pkndelta_05':pkndelta_05,'taukndelta_05':taukndelta_05}
json = json.dumps(dict)
f= open("bintree_simu_results.json","w")
f.write(json)
f.close()

