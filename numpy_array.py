import numpy as np
a=np.array([[1,1,1],[0,4,-1],[2,-2,1]])
print(a)
print("a.ndm",a.ndim)
b=np.array([6,5,1])
print(b)
c = np.linalg.solve(a,b)
print("type c",type(c))
print("a/b=",c)

for i in c :
    print(i)
    print(type(i))