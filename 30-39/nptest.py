import numpy as np


a=np.random.randint(0,10, (10,10)).astype(np.int32)

print(a)

b=a==3
c=np.where(a==3)

print(b)
print(c)