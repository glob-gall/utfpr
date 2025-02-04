import numpy as np

m = np.array(eval(input()))
f = np.array(eval(input()))
ch = np.array(eval(input()))

vet = np.zeros(3, dtype=int)

for i in range(np.size(m)):
    if m[i] >= 5.0 and f[i] >= 0.75 * ch[i]:
        vet[0] += 1
    elif m[i] < 5.0 and f[i] >= 0.75 * ch[i]:
        vet[1] += 1
    elif m[i
