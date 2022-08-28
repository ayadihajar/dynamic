
def meta1(seq,p,d):
    from random import randint
    import time
    n=len(seq)
    def retard(x):
        pPrec=0
        u=0
        for i in x:
            pPrec+=p[i-1]
            if pPrec>d[i-1]:
                u+=1
            else:
                u+=0
        return u

    def InsertionOperator(l):
        n=len(l)
        x=[]
        i,j=0,0
        while i==j:
            i=randint(0,n-1)
            j=randint(0,n-1)
        if i<j:
            x=(l[0:i]+l[i+1:j+1]+l[i:i+1]+l[j+1:n+1])
        else:
            x=(l[0:j]+l[i:i+1]+l[j:i]+l[i+1:n+1])
        return x

    def SwapOperator(l):
        n,i,j=len(l),0,0
        x=l.copy()
        while i==j:
            i=randint(0,n-1)
            j=randint(0,n-1)
        x[i],x[j]=x[j],x[i]
        return x

    def opt2OperatorF(l):
        n=len(l)
        i=randint(0,n-4)
        j=randint(i+2,n-2)
        new_seq=l[0:i+1]+l[j:i:-1]+l[j+1:n]
        return new_seq


    structV=[opt2OperatorF,SwapOperator,InsertionOperator]


    def EDD(x):
        return [k for k in sorted(x, key=lambda k: d[k-1])]
    def VND(s,end):
        l=0
        x=s.copy()
        start2=time.time()
        while (l<3 and time.time()-start2 < len(seq)*end):
            x1=structV[l](x)
            if retard(x1)<retard(x):
                x=x1[:]
                l=0
            else:
                l+=1
        return x
    
    def GVNS(seq,end):
        start=time.time()
        x=seq.copy()
        
        while time.time()-start< len(seq)*end:
                k=0        
                while k<3:
                    x1=structV[k](x)#Shaking
                    x2=VND(x1,0.5)#The best neighbor
                    if retard(x2)<retard(x):
                        x=x2.copy()
                        k=0
                    else:
                        k+=1
        return x

    seq = EDD(seq)
    seq = VND(seq, 0.1)#optimisation de la solution initiale
    x=GVNS(seq, 0.1)
    return [x,retard(x),3]
