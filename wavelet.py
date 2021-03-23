import math

from simplestat import mean

#def basis(n=3):
#    return [unit(i) for i in range(n)]
#def unit(i):
#    ret=[]
#    while len(ret)<i:ret.append(0.0)
#    ret.append(1.0)
#    return wavelet(*ret)

def theta(x):
    if x<0.5:
        return -1.0
    elif x==0.5:
        return 0.0
    else:
        return 1.0

def linear(x):
    return (x-0.5)

def cube(x):
    return (x-0.5)**3

def sigmoid(alpha):
    def sig(x):
        return (1/(1+math.exp(-alpha*x)))-0.5
    return sig

class wavelet(object):
    #r1=-1.0#ranges for the orthogonality
    #r2=1.0
    #epsilon=0.001
    r1=0.0
    r2=0.999
    epsilon=0.01
    
    
    def __init__(s,f):
        s.f=f
    
    def __add__(a,b):
        def ret(x):
            return a.f(x)+b.f(x)
        return wavelet(ret)
    def __sub__(a,b):
        def ret(x):
            return a.f(x)-b.f(x)
        return wavelet(ret)
    __rsub__=__sub__
    
    def __getitem__(s,x):
        return s.f(x)

    def x(s):
        ret=[]
        ac=s.r1
        while ac<=s.r2:
            ret.append(ac)
            ac+=s.epsilon
        return ret
    def y(s):
        return [s.f(x) for x in s.x()]
    def absmean(s):
        return mean([abs(zw) for zw in s.y()])
    def scalar(a,b):
        ret=0.0
        for x in a.x():
            ret+=a.f(x)*b.f(x)
        return ret
    def multwithfloat(s,f):
        def ret(x):
            return s.f(x)*f
        return wavelet(ret)
    
    def __mul__(a,b):
        if type(a) is int:a=float(a)
        if type(b) is int:b=float(b)
        if type(a) is float:
            if type(b) is float:
                raise Exception("THIS SHOULD NOT HAPPEN")
            else:
                return b.multwithfloat(a)
        else:
            if type(b) is float:
                return a.multwithfloat(b)
            else:
                return a.scalar(b)
    __rmul__=__mul__

    def __repr__(s):
        return str(s)
    def __str__(s):
        return "some wavelet"#"+".join([str(q)+"x**"+str(i) for i,q in enumerate(s.q) if not q==0.0])

class unitlet(wavelet):
    r1=0.0
    r2=0.999
    epsilon=0.01

if __name__=="__main__":
    from graham import *
    from plt import *
    b=[sigmoid(5),linear,cube]

    b=[sigmoid(i) for i in [3,5,7]]

    b=[wavelet(zw) for zw in b]
    bo=findorthonormal(*b)
    #bo=b

    print(scalarmat(*bo))

    for zw in bo:
        plt.plot(zw.x(),zw.y())
    plt.show()
    


