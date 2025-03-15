#1
import numpy as np
import time
N, M = int(input()),int(input())
A = np.random.rand(N, M)
start = time.time()
stroka = np.mean(A, axis=1)
end = time.time()
print(np.max(stroka))
print(end-start)
#1 без numpy
import random
N, M = int(input())
A = [[random.random() for _ in range(M)] for _ in range(N)]
start = time.time()
stroka = [sum(stroka) / M for stroka in A]
maxi = max(stroka)
end = time.time()
print(maxi)
print(end - start)

#2

N, M = int(input()), int(input())
A = np.random.rand(N, M)
start = time.time()
summ = np.sum(np.abs(A), axis=1)
maxim = np.argmax(summ)
end = time.time()
print(np.min(A[maxim]))
print(end - start)

#3
N, M = int(input()), int(input())
A = np.random.rand(N, M)
start = time.time()
row = np.mean(A, axis=0)
end = time.time()
print(np.min(row))
print(end - start)

#4
N, M = int(input()),int(input())
A = np.random.rand(N, M)
start = time.time()
stroka = np.mean(A, axis=1)
stolb = np.mean(A, axis=0)
matrix = np.mean(A)
end = time.time()
print(stroka)
print(stolb)
print(matrix)
print(end-start)


#5
N, M = int(input()), int(input())
A = np.random.rand(N, M)
B = A[:228, :228]
chislo = int(input())
start = time.time()
B *= chislo
end = time.time()
print(B)
print(end-start)
