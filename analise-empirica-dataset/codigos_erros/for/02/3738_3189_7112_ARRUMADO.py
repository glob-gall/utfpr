import numpy as np

a = np.array(eval(input()))
b = np.array(eval(input()))
c = float(input())

CH = 0.75 * c

Vet = np.zeros(3, dtype=int)

for i in range(np.size(a)):
    if a[i] >= 5.0 and b[i] >= CH:
        Vet[0] += 1
    if a[i] < 5.0:
        Vet[1] += 1
    if b[i] < CH:
        Vet[2] += 1

print(Vet)
