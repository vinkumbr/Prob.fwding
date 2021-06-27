import json
import numpy as np

# From simulations
delta = 0.1
k = 20
#n=20:1:40

#Results of probabilistic forwarding for a hypercube of d = 12 bits (2^12 nodes) with k=20 packets and n varying from 20 to 60 in steps of 1
d = 12
pkndelta = [0.39,0.32,0.28,0.255,0.235,0.223,0.213,0.206,0.198,0.1925,0.1885,0.185,0.183,0.1786, 0.1766,0.1726,0.1707,0.1679,0.1665,0.1651,0.163,0.1614,0.16,0.1584,0.1574,0.1556,0.1546,0.1538, 0.1531,0.1518,0.151,0.15005,0.14935,0.14865,0.14845,0.14796,0.14696,0.1464,0.14572,0.14494,0.14434]
tau_kndelta = [31729.98, 26992.73, 23952.11, 22298.81, 20712.43, 20079.8, 19193.82, 18769.86, 18023.02, 17641.59, 17382.9, 17194.04, 17399.5, 16833.23, 16934.98, 16562.13, 16442.6, 16209.93, 16411.9, 16299.54, 15863.85, 15887.06, 15374.49, 15486.97, 15638.25, 15394.08, 15472.18, 15311.53, 15169.47, 15009.43, 15306.8, 14798.19, 14558.65, 14861.62, 15217.8, 15194.31, 15170.92, 14730.48, 14643.48, 14791.28, 14597.42]

#Results of probabilistic forwarding for a hypercube of d = 10 bits (2^10 nodes) with k=20 packets and n varying from 20 to 60 in steps of 1
d1 = 10
pkndelta1 = [0.47,0.37,0.33,0.295,0.278,0.269,0.255,0.245,0.238,0.231,0.226,0.222,0.2175,0.214,0.2114,0.208, 0.2071, 0.2044,0.2016,0.1988,0.1978]
tau_kndelta1 = [9576.69, 7820.13, 7112.17, 6459.95, 6046.95, 6120.29, 5798.4, 5588.24, 5439.01, 5352.62, 5300.28, 5234.26, 5087.4, 5024.64, 5138.73, 4932.15, 5050.13, 5017.53, 4969.7, 4813.89, 4787.65]

#Results of probabilistic forwarding for a hypercube of d = 12 bits (2^12 nodes) with k=20 packets and n varying from 200 to 300 in steps of 10
pkndelta_inc = [0.1219,0.1214,0.1206,0.1199,0.1194,0.119,0.1185,0.118,0.1176,0.1171,0.117]
tau_kndelta_inc = [14210.57, 14318.51, 14156.84, 13999.1, 14205.57, 14168.78, 14247.16, 13995.28, 14213.78, 14131.67, 14775.07]

#Results of probabilistic forwarding for a hypercube of d = 12 bits (2^12 nodes) with k=20 packets and n varying from 200 to 700 in steps of 50
pkndelta_long = [0.1219,0.119,0.117,0.1153,0.1134,0.1123,0.1112,0.1103,0.1094,0.1085,0.108]
tau_kndelta_long = [14211.24, 14459.91, 14693.73, 15200.3, 14571.26, 15328.37, 15529.9, 15829.66, 16409.48, 16496.32, 17127.47]

#Results of probabilistic forwarding for a hypercube of d = 10 bits (2^10 nodes) with k=20 packets and n varying from 200 to 700 in steps of 50
pkndelta1_long = [0.1442,0.1394,0.1362,0.1331,0.1308,0.1286,0.1267,0.1252,0.1238,0.1222,0.1213]
tau_kndelta1_long = [4897.11, 5142.28, 5359.46, 5574.17, 5858.81, 6003.34, 6153.71, 6454.85, 6740.86, 6846.37, 7100.95]

dict={"k":str(k),"d":str(d),"pkndelta":pkndelta[:21],"tau_kndelta":tau_kndelta[:21], "d1":str(d1),"pkndelta1":pkndelta1,"tau_kndelta1":tau_kndelta1,"pkndelta_long":pkndelta_long, "tau_kndelta_long":tau_kndelta_long,"pkndelta1_long":pkndelta1_long, "tau_kndelta1_long":tau_kndelta1_long}
json = json.dumps(dict)
f= open("hypercube_simu_results.json","w")
f.write(json)
f.close()
