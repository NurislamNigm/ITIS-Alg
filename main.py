import numpy as np

z1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(z1)

z2 = np.zeros(7)
print(z2)

z3 = np.ones(5)
print(z3)

z4 = np.arange(10, 51, 5)
print(z4)

z5 = np.linspace(0, 100, 6)
print(z5)

z6 = np.array([1, 2, 3, 4, 5, 6, 7])
print(z6[1])
print(z6[-1])
print(z6[3:7])


z7 = np.array([1, 2, 3, 4, 5])
for i in z7:
    print(i)

z81 = np.array([1, 2, 3])
z82 = np.array([1, 2, 3])
summm = z81+z82
print(summm)

z9 = np.array([1, 2, 3, 4, 5])
z99 = z9 * 2
print(z99)

z10 = np.array([1, 2, 3, 4, 5])
z100 = z10 ** 2
print(z100)

z11 = np.array([1, 2, 3])
print(np.min(z11))
print(np.max(z11))

z12 = np.array([1, 2, 3, 4, 5])
print(np.mean(z12))
print(np.std(z12))

z13 = np.array([1, 2, 3, 4, 5])
print("log",np.log(z13))
print("exp", np.exp(z13))
print("sin", np.sin(z13))

z14 = np.random.rand(10)
print(z14)

z15 = np.random.randint(1, 101, 6)
print(z15)

z16 = np.arange(1, 11)
z32 = z16.reshape(2, 5)
print(z32)

z17 = np.arange(1, 10)
z177 = z17.reshape(3, 3)
print(z177)

z18 = np.array([1, 6, 3, 8, 2, 9])
z188 = z18[z18 > 5]
print(z188)

def funct(x):
    return x**3

z19 = np.array([1, 2, 3, 4, 5])
cube = np.vectorize(funct)
z19cube = cube(z19)
print(z19cube)

z20 = np.array([1, 2])
np.save('z20.npy', z20)
filez20 = np.load('array.npy')
print(filez20)