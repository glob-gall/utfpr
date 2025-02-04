import numpy as np

v = np.array(eval(input()))
f = np.array(eval(input()))
c = int(input())
v1 = np.zeros(3, dtype=int)

a = c * 75 / 100
A = 0
N = 0
F = 0

for i in range(np.size(v)):
    if v[i] < 5:
        N += 1
    if f[i] < a:
        F += 1
    if v[i] >= 5 and f[i] >= a:
        A += 1

v1[0] = A
v1[1] = N
v1[2] = F

print(v1)
