def dyn1(jobs,p,dD):
    from itertools import combinations
    f=dict()
    pP=dict()
    n=len(jobs)
    s=dict()
    #Conditions initiales
    k=0
    for i in range(n):
        pP[(i+1,)]=p[i]
    for i in range(n):
        if p[i]>dD[i]:
            f[(i+1,)]=1
        else:
            f[(i+1,)]=0
    #traitment
    for i in range(1,n):   
        for j in combinations(jobs,i+1):
            min=1000000
            for r in range(i+1):
                a=j[r]
                aux=list(j).copy()
                aux.remove(a)
                aux=tuple(aux)
                pP[j]=pP[(a,)]+pP[aux]
                if pP[j]>dD[a-1]:
                    u=1
                else:
                    u=0
                if (f[aux]+u)<min:
                    min=f[aux]+u
                    s[j]=a  
            f[j]=min
    sec=[0]*(n-1)
    m=jobs.copy()
    sequence=[]
    for k in range(0,1-n,-1):
        sec[-1+k]=s[tuple(m)]
        m.remove(s[tuple(m)])
    #A la fin m contient le premier élément de notre liste
    sequence=m[0:1]+sec[0:]
    return [sequence,min,3]