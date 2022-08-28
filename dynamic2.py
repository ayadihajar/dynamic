def dyn2(jobs,p,dD,a,b):
    from itertools import combinations
    n=len(jobs)
    pP,f,s={},{},{}
    #Remplissage pour des séquences de 1 seule tâche
    for i in range(n):
        pP[(i+1,)]=p[i]
        f[(i+1,)]=a[i]*max(0,dD[i]-p[i])+b[i]*max(0,p[i]-dD[i])
    #Traitement principal:    
    for i in range(1,n):
        for j in combinations(jobs,i+1):
            min=100000
            for r in range(i+1):
                eltD=j[r]
                aux=list(j).copy()
                aux.remove(eltD)
                aux=tuple(aux)
                j=tuple(j)
                pP[j]=pP[aux]+p[eltD-1]
                act=a[eltD-1]*max(0,dD[eltD-1]-pP[j])+b[eltD-1]*max(0,pP[j]-dD[eltD-1])+f[aux]
                if act<min:
                    f[j]=act
                    min=act
                    s[j]=eltD
    aux=[]
    for i in range(n-1):
        a=s[j]
        aux.append(a)
        j=list(j)
        j.remove(a)
        j=tuple(j)
    aux=list(reversed(aux))
    aux.insert(0,j[0])
    return [aux,min,5]