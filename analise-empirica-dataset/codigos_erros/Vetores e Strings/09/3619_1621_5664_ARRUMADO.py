from numpy import *

p = array(eval(input().upper()))
q = array(eval(input()))

a = 0
b = 0
c = 0
d = 0
e = 0
i = 0
while i < size(p):
    if p[i] == 'ARROZ':
        a += 1.25 * q[i]
    elif p[i] == 'FEIJAO':
        b += 2.6 * q[i]
    elif p[i] == 'BIS':
        c += 1.8 * q[i]
    elif p[i] == 'MIOJO':
        d += 0.85 * q[i]
    elif p[i] == 'FANTA':
        e += 3.20 * q[i]
    i += 1

soma = a + b + c + d + e
print(soma)
