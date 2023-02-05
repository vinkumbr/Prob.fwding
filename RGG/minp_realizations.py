import numpy as np
import scipy.stats as st
import json
import datetime

nstart = 20
nstop = 40
ci = np.zeros([nstop-nstart+1,3])
count = 0
k = 20
for n in range(nstart,nstop+1):
    with open("./realization_results/recs_all_realizations_lbda4_id%d.json"%(n),'r') as f:
        data = json.load(f)
        pstart = data['pstart']
        pstop = data['pstop']
        pstep = data['pstep']
        frac_R_succ_p = data['frac_R_succ_p']
        delta = data['delta']
    frac_R_succ_p = np.asarray(frac_R_succ_p)
    a,iter = frac_R_succ_p.shape
    cirec = np.zeros([a,3])
    for i in range(a):
        cirec[i,0],cirec[i,2] = st.norm.interval(alpha=0.95,loc=np.mean(frac_R_succ_p[i]),scale=st.sem(frac_R_succ_p[i]))
        cirec[i,1] = np.mean(frac_R_succ_p[i])
    #print(cirec)
    p = np.arange(pstart,pstop+pstep/2,-pstep)
    plong = np.linspace(pstart,pstop,10000)
    minp = np.zeros(3)
    for j in range(3):
        interp_cirec = np.interp(np.flip(plong),np.flip(p),np.flip(cirec[:,j]))
        #print(interp_cirec)
        pidx = np.where(np.flip(interp_cirec)<1-delta)[0]
        #print(pidx)
        if pidx.size == 0:
            minp[j] = plong[-1]
        else:
            minp[j] = plong[pidx[0]+1]
    #print(minp)
    ci[count,:] = minp
    count += 1
print(ci)
time = datetime.datetime.now()
dict = {'time':str(time),'lbda':4,'nstart':nstart,'nstop':nstop,'k':k,'conf_interval_pkndelta':ci.tolist()}
json = json.dumps(dict)
g = open('conf_intervals4.json','w')
g.write(json)
g.close()