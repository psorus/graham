import numpy as np
import math

from tqdm import tqdm


f=np.load("cut.npz")

q=f["q"]

n=5

#q=q[:n]


from wavelet import *
from graham import *

from simplestat import mean,statinf

def arraytofunc(arr):
    def f(x):
        return arr[int(x*len(arr))]
    return f
def arraytolet(arr):
    m=mean(arr)
    arr=[zw-m for zw in arr]
    return unitlet(arraytofunc(arr))


l=[arraytolet(list(ac)) for ac in q]



from plt import *

for zw in l[:n]:
    plt.plot(zw.x(),zw.y())

plt.show()

lo=findorthonormal(*l[:n])
#print(scalarmat(*l))
#print(scalarmat(*lo))


def rectest(q):
    q*=1/math.sqrt(q*q)

    alphas=[q*zw for zw in lo]

    ret=None
    for alpha,qq in zip(alphas,lo):
        #print(type(alpha),type(qq))
        ac=alpha*qq
        if ret is None:
            ret=ac
        else:
            ret+=ac
    #print(type(ret),type(q))
    return (ret-q).absmean()

for zw in lo:
    plt.plot(zw.x(),zw.y())
plt.show()

recs=[]
for zw in tqdm(l[n:]):
    recs.append(rectest(zw))

print(statinf(recs))

#for i in range(n+3):
#    print(rectest(l[i]))



