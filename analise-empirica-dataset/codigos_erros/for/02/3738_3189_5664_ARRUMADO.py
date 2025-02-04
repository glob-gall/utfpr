import numpy as np

m = np.array(eval(input()))
p = np.array(eval(input()))
c = int(input())

cont = np.zeros(3, dtype=int)
f = c * 75 / 100

for i in range(np.size(m)):
    if m[i] >= 5 and p[i] >= f:
        cont[0] += 1
    elif m[i] < 5:
        cont[1] += 1
    elif p[i] < f:
        cont[2] += 1

print(cont)
