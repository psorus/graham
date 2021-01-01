

def basis(n=3):
  return [unit(i) for i in range(n)]
def unit(i):
  ret=[]
  while len(ret)<i:ret.append(0.0)
  ret.append(1.0)
  return poly(*ret)


class poly(object):
  r1=0.0#ranges for the orthogonality
  r2=1
  
  
  def __init__(s,*q):
    s.q=q
  
  def ql(s,l):
    ret=list(s.q)
    
    while len(ret)<l:
      # ret.insert(0,0)
      ret.append(0.0)
    return ret
  
  def __len__(s):
    return len(s.q)
  
  def __add__(a,b):
    qa=a.ql(len(b))
    qb=b.ql(len(a))
    return poly(*[pa+pb for pa,pb in zip(qa,qb)])
  def __subtr__(a,b):
    return a+(b*-1)
  
  def scalar(a,b):
    qa=a.ql(len(b))
    qb=b.ql(len(a))
    rel=[0 for i in range(2*len(qb))]
    for ia,aa in enumerate(qa):
      for ib,bb in enumerate(qb):
        rel[ia+ib]+=aa*bb
      
    return poly(*rel).intfrom(a.r1,a.r2)
  def multwithfloat(s,f):
    return poly(*[q*f for q in s.q])
  
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

  def int(s,x0=0.0):
    return poly(x0,*[q/(i+1) for i,q in enumerate(s.q)])

  def eval(s,x):
    ret=0.0
    for zw in [q*x**i for i,q in enumerate(s.q)]:
      ret+=zw
    return ret

  def __getitem__(s,key):
    return s.eval(key)

  def delta(s,x1,x2):
    return s[x2]-s[x1]
  
  def intfrom(s,x1,x2):
    S=s.int()
    return S.delta(x1,x2)
  
  def __repr__(s):
    return str(s)
  def __str__(s):
    return "+".join([str(q)+"x**"+str(i) for i,q in enumerate(s.q) if not q==0.0])
  