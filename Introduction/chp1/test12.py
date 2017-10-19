import numpy as np
mylist = [1,2,3]
x = np.array(mylist)
print(x)

y = np.array([4,5,6])
print(y)

m = np.array([[7,8,9],[10,11,12]])
print(m)

print(m.shape)

n = np.arange(0,30,2)
print(n)

n = n.reshape(3,5)
print(n)

o = np.linspace(0,4,9)
print(o)

o.resize(3,3)
print(o)

print(np.ones((3,2)))
print(np.zeros((2,3)))
print(np.eye(3))
print(np.diag(y))

print(np.array([1,2,3] * 3))
print(np.repeat([1,2,3],3))

p = np.ones((2,3))
print(p)
print(np.vstack([p,2*p]))
print(np.hstack([p,2*p]))

print(x+y)
print(x * y)
print(x ** 2)
print(x.dot(y))
print(np.matmul(x,y))

