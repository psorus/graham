import copy
import math

#still requires the case that q*q=0 (permute), also a trafo matrix would be nice and using this https://en.wikipedia.org/wiki/Arnoldi_iteration you migth be able to solve numerical problems

def findorthogonal(*q):
    """finds an orthogonal basis for the vector room spanned by the objects in q"""
    ret=[]
    for i,o in enumerate(q):
        ac=copy.copy(o)
        for zw in ret:
            mul=(zw*o)/(zw*zw)
            ac-=mul*zw
        ret.append(ac)
    return ret
def findorthonormal(*q):
    """finds an orthonormal basis for the vector room spanned by the objects in q"""
    ret=[]
    for i,o in enumerate(q):
        ac=copy.copy(o)
        for zw in ret:
            mul=(zw*o)
            ac=ac+(-1*mul*zw)
        mul2=1/math.sqrt((ac*ac))
        ret.append(ac*mul2)
    return ret

def scalarmat(*q):
    """multiplies every object in q with each object in q. Should return a unity matrix for an orthonormal system"""
    ret=[]
    for a in q:
        toa=[]
        for b in q:
            toa.append(a*b)
        ret.append(toa)
    return ret

def maxdiffident(q):
    """maximum difference of each element to the identity"""
    m=0.0
    for i,a in enumerate(q):
        for j,b in enumerate(a):
            shall=0.0
            if i==j:shall=1.0
            d=abs(shall-b)
            if d>m:m=d
    return m

