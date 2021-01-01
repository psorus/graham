import numpy as np

from poly import *
from graham import *

# k=unit(1)

# print(k)

# print(poly(*k.ql(10)))

# exit()


b=basis(5)

for bb in b:
  print(bb)

print("orthonormating...")

bo=findorthonormal(*b)
for bb in bo:
  print(bb)

print(bo[-1].q)

print(np.array(scalarmat(*bo)))
print(maxdiffident(scalarmat(*bo)))

exit()



x=poly(1,2,3)

print(x*x)
print(x*3)
print(3*x)

exit()


print(x)
X=x.int()

print(X)

print(x.intfrom(-1,1))

