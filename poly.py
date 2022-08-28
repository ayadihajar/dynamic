def polynomial(jobs,p,dD):
    #EDD
    i,n=0,len(jobs)
    while(i<n-1):
        if dD[i]>dD[i+1]:
            dD[i],dD[i+1]=dD[i+1],dD[i]
            p[i],p[i+1]=p[i+1],p[i]
            jobs[i],jobs[i+1]=jobs[i+1],jobs[i]
            if (not(i==0)):
                i-=1
        else:
            i+=1
    #Moore & hangdson
    S=[]
    som,max,act,prec,b=0,-1,0,0,0
    for i in range(n):
                S.append(jobs[i]) 
                som+=p[i]
                if som>dD[i]:
                    if p[i]>p[jobs.index(S[act])]:
                        act=len(S)-1
                    som-=p[jobs.index(S[act])] 
                    S.remove(S[act])
                    act=prec
                else:
                    if max<p[i] :
                        max=p[i]
                        if len(S)>1:
                            prec=act
                            act=len(S)-1 
    return[len(jobs)-len(S),S,list(set(jobs)-set(S))]
