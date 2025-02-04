import numpy as np

nvet = np.array(eval(input()))
fvet = np.array(eval(input()))
c = float(input())
aux = np.zeros(3, dtype=int)
ap = 0
rpn = 0
rpf = 0

for i in range(len(nvet)):
    if nvet[i] >= 5.0 and fvet[i] >= 0.75 * c:
        ap += 1
    elif nvet[i] >= 5.0 and fvet[i] < 0.75 * c:
        rpf += 1
    elif nvet[i] < 5.0 and fvet[i] >= 0.75 * c:
        rpn += 1

aux[0] = ap
aux[1] = rpn
aux[2] = rpf
print(aux)
