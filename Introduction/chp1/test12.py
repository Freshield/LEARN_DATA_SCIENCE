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

z = np.array([y,y**2])
print(z)

print(z.shape)
print(z.T)
print(z.T.shape)

print(z.dtype)
z = z.astype('f')
print(z.dtype)

a = np.array([-4,-2,1,3,5])
print(a.sum())
print(a.max())
print(a.min())
print(a.mean())
print(a.std())

print(a.argmax())
print(a.argmin())

s = np.arange(13) ** 2
print(s)

print(s[0],s[4],s[0:3])
print(s[1:5])
print(s[-4:])

print(s[-5::-2])

r = np.arange(36).reshape((6,6))
print(r)

print(r[2,2])
print(r[3,3:6])
print(r[:2,:-1])

print(r[-1,::2])

print(r[r > 30])

r[r > 30] = 30
print(r)

r2 = r[:3,:3]
print(r2)

r2[:] = 0
print(r)

r_copy = r.copy()
print(r_copy)

r_copy[:] = 0
print(r_copy)

print(r)

test = np.random.randint(0,10,(4,3))
print(test)

for row in test:
    print(row)

for i in range(len(test)):
    print(test[i])

for i,row in enumerate(test):
    print('row',i,'is',row)

test2 = test ** 2
print(test2)

for i,j in zip(test,test2):
    print(i,'+',j,'=',i+j)

print(['a','b','c']+[1,2,3])

print(type(lambda x:x+1))