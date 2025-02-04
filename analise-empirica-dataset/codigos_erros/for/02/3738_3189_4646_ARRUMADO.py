import numpy as np

notas = np.array(eval(input()))
fr = np.array(eval(input()))
ch = int(input())
fa = ch * 75 / 100
s = np.zeros(3, dtype=int)

for i in range(np.size(notas)):
    if notas[i] >= 5 and fr[i] >= fa:
        s[0] += 1
    elif notas[i] < 5 and fr[i] >= fa:
        s[1] += 1
    elif notas[i] >= 5 and fr[i] < fa:
        s[2] += 1

print(s)
