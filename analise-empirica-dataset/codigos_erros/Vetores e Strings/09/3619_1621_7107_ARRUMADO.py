from numpy import *

vn = array(eval(input()))
vq = array(eval(input()))
i = 0
t = 0
custo = [1.25, 2.60, 1.80, 0.85, 3.20]

while i < size(vn):
    if vn[i] == "ARROZ":
        c = custo[0] * vq[i]
    elif vn[i] == "FEIJAO":
        c = custo[1] * vq[i]
    elif vn[i] == "BIS":
        c = custo[2] * vq[i]
    elif vn[i] == "MIOJO":
        c = custo[3] * vq[i]
    elif vn[i] == "FANTA":
        c = custo[4] * vq[i]
    t = t + c
    i = i + 1

print(t)
