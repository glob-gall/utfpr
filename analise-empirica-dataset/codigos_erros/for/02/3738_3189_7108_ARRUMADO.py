import numpy as np

mf = np.array(eval(input()))
p = np.array(eval(input()))
ch = int(input())
cont = np.zeros(3, dtype=int)

for a in range(np.size(mf)):
    if mf[a] >= 5.0 and p[a] >= 0.75 * ch:
        cont[0] += 1
    elif mf[a] < 5.0 and p[a] >= 0.75 * ch:
        cont[1] += 1
    elif mf[a] >= 5.0 and p[a] < 0.75 * ch:
        cont[2] += 1

print(cont)
